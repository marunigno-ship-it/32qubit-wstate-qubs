from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
import numpy as np

n = 32
shots = 1024

qc = QuantumCircuit(n + 1)
qc.h(0)
for i in range(1, n + 1):
    theta = 2 * np.arcsin(1 / np.sqrt(i))
    qc.ry(theta, i - 1)
    qc.cx(0, i - 1)
qc.measure_all()

sim = AerSimulator()
circ = transpile(qc, sim)
job = sim.run(circ, shots=shots)
counts = job.result().get_counts()
print("32-Qubit W State Counts:", counts)
