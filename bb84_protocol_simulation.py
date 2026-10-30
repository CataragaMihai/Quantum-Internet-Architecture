from qiskit import QuantumCircuit, transpile
from qiskit.providers.basic_provider import BasicSimulator
import numpy as np


def encode_messages(bits, bases):
    """Prepare one qubit circuit for each bit and its chosen basis."""
    if len(bits) != len(bases):
        raise ValueError("bits and bases must have the same length")

    circuits = []
    for bit, basis in zip(bits, bases):
        if bit not in (0, 1) or basis not in (0, 1):
            raise ValueError("bits and bases must contain only 0 or 1")

        qc = QuantumCircuit(1, 1)
        if basis == 0:
            if bit:
                qc.x(0)
        elif bit == 0:
            qc.h(0)
        else:
            qc.x(0)
            qc.h(0)
        circuits.append(qc)
    return circuits


def measure_message(circuits, bases):
    """Copy each circuit and measure it in Bob's chosen basis."""
    if len(circuits) != len(bases):
        raise ValueError("circuits and bases must have the same length")

    measured_circuits = []
    for qc, basis in zip(circuits, bases):
        if basis not in (0, 1):
            raise ValueError("bases must contain only 0 or 1")
        measured_qc = qc.copy()
        if basis == 1:
            measured_qc.h(0)
        measured_qc.measure(0, 0)
        measured_circuits.append(measured_qc)
    return measured_circuits


def remove_trash(alice_bases, bob_bases, bits):
    """Keep the bits measured in matching bases."""
    if not (len(alice_bases) == len(bob_bases) == len(bits)):
        raise ValueError("bases and bits must have the same length")
    return [bit for i, bit in enumerate(bits) if alice_bases[i] == bob_bases[i]]


def create_full_circuit(alice_bits, alice_bases, bob_bases):
    """Build one circuit diagram showing the whole exchange."""
    n_qubits = len(alice_bits)
    if not (len(alice_bases) == len(bob_bases) == n_qubits):
        raise ValueError("bits and bases must have the same length")

    qc = QuantumCircuit(n_qubits, n_qubits)
    for i, (bit, basis) in enumerate(zip(alice_bits, alice_bases)):
        if bit not in (0, 1) or basis not in (0, 1) or bob_bases[i] not in (0, 1):
            raise ValueError("bits and bases must contain only 0 or 1")
        if basis == 0:
            if bit:
                qc.x(i)
        elif bit == 0:
            qc.h(i)
        else:
            qc.x(i)
            qc.h(i)

    qc.barrier()
    for i, basis in enumerate(bob_bases):
        if basis == 1:
            qc.h(i)
        qc.measure(i, i)
    return qc


def bb84_protocol(n_bits=16, seed=0):
    """Run BB84 locally with Qiskit's built-in simulator."""
    if n_bits < 1:
        raise ValueError("n_bits must be at least 1")

    rng = np.random.default_rng(seed)
    alice_bits = rng.integers(2, size=n_bits).tolist()
    alice_bases = rng.integers(2, size=n_bits).tolist()
    bob_bases = rng.integers(2, size=n_bits).tolist()

    message = encode_messages(alice_bits, alice_bases)
    bob_circuits = measure_message(message, bob_bases)
    full_circuit = create_full_circuit(alice_bits, alice_bases, bob_bases)

    simulator = BasicSimulator()
    compiled = transpile(bob_circuits, simulator)
    job = simulator.run(compiled, shots=1)
    counts_list = job.result().get_counts()
    bob_results = [int(next(iter(counts)), 2) for counts in counts_list]

    return {
        "alice_bits": alice_bits,
        "alice_bases": alice_bases,
        "bob_bases": bob_bases,
        "bob_results": bob_results,
        "alice_key": remove_trash(alice_bases, bob_bases, alice_bits),
        "bob_key": remove_trash(alice_bases, bob_bases, bob_results),
        "job_id": job.job_id(),
        "full_circuit": full_circuit,
    }


def analyze_results(results):
    print("Initial values:")
    print(f"Alice's bits: {results['alice_bits']}")
    print(f"Alice's bases: {results['alice_bases']}")
    print(f"Bob's bases: {results['bob_bases']}")
    print(f"Bob's results: {results['bob_results']}")
    print("\nGenerated keys:")
    print(f"Alice's key: {results['alice_key']}")
    print(f"Bob's key: {results['bob_key']}")

    if results["alice_key"] == results["bob_key"]:
        print("\nSuccess: keys match")
    else:
        errors = sum(a != b for a, b in zip(results["alice_key"], results["bob_key"]))
        qber = errors / len(results["alice_key"]) if results["alice_key"] else 0
        print(f"\nWarning: keys differ (QBER: {qber:.2%})")

    print(f"\nLocal simulator job ID: {results['job_id']}")
    print("\nFull circuit:")
    print(results["full_circuit"])


if __name__ == "__main__":
    try:
        print("Running BB84 on Qiskit's local simulator:")
        analyze_results(bb84_protocol(n_bits=16))
    except Exception as exc:
        print(f"Error: {exc}")
