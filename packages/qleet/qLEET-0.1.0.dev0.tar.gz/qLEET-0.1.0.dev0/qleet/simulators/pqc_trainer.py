import typing

import cirq
import tqdm.auto as tqdm

import tensorflow as tf
import tensorflow_quantum as tfq

from ..interface.metas import AnalyzerList
from ..interface.circuit import CircuitDescriptor


class PQCSimulatedTrainer:
    """A class to train parametrized Quantum Circuits in Tensorflow Quantum
    Uses gradient descent over the provided parameters, using the TFQ Adjoin differentiator.
    """

    def __init__(self, circuit: CircuitDescriptor):
        self.optimizer = tf.keras.optimizers.Adam(lr=0.01)
        self.pqc_layer = tfq.layers.PQC(
            circuit.cirq_circuit,
            circuit.cirq_cost,
            differentiator=tfq.differentiators.Adjoint(),
        )
        self.model = tf.keras.models.Sequential(
            [tf.keras.layers.Input(shape=(), dtype=tf.dtypes.string), self.pqc_layer]
        )
        self.circuit = circuit

    def train(self, n_samples=100, loggers: typing.Optional[AnalyzerList] = None):
        dummy_input = tfq.convert_to_tensor([cirq.Circuit()])
        total_error = 0.0
        with tqdm.trange(n_samples) as iterator:
            iterator.set_description("QAOA Optimization Loop")
            for step in iterator:
                with tf.GradientTape() as tape:
                    error = self.model(dummy_input)
                grads = tape.gradient(error, self.model.trainable_variables)
                self.optimizer.apply_gradients(
                    zip(grads, self.model.trainable_variables)
                )
                error = error.numpy()[0][0]
                if loggers is not None:
                    loggers.log(self, error)
                total_error += error
                iterator.set_postfix(error=total_error / (step + 1))
        return self.model

    def evaluate(self, n_samples: int = 1000):
        dummy_input = tfq.convert_to_tensor([cirq.Circuit()])
        total_error = 0.0
        with tqdm.trange(n_samples) as iterator:
            iterator.set_description("QAOA Evaluation Loop")
            for step in iterator:
                error = self.model(dummy_input)
                error = error.numpy()[0][0]
                total_error += error
                iterator.set_postfix(error=total_error / (step + 1))
        return total_error / n_samples
