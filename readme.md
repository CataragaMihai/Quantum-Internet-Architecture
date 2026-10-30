# The Architecture of a Quantum Internet

This repository contains my analysis article entitled "The Architecture of a Quantum Internet". Said article studies topics such as quantum computing and quantum key distribution (QKD), and it was presented at the UTM student conference (*Conferința Tehnico-Științifică a Studenților, Masteranzilor și Doctoranzilor*, Technical University of Moldova, Chișinău, 13–16 May 2026). Along with the article, the file bb84_protocol_simulation.py runs a Python program using the Qiskit SDK to showcase how the BB84 QKD protocol mentioned in the article functions.

## The article

the-architecture-of-a-quantum-internet.pdf

This is a revised version (October 2026) of the paper presented at the conference: a few statements were corrected, and the sources and image credits were made more precise.

**Abstract.** The current internet infrastructure is based on the classical binary system, which has fundamental limitations in computational power and cybersecurity. Recent quantum computing advancements confirm that quantum systems have a massive advantage over even supercomputers on certain tasks. For example, Google’s 70-qubit Sycamore processor completed in seconds a benchmark calculation that would have required approximately 50 years on the most advanced supercomputer. In the future, larger quantum computers could pose a direct threat to modern encryption. Using Shor’s algorithm, a sufficiently powerful quantum computer could render RSA encryption useless. This creates an urgent need for systems that guarantee security over communication channels. Alongside post-quantum cryptography, Quantum Key Distribution addresses this problem by using single photons or entangled photon pairs to generate shared encryption keys. Any eavesdropping attempt in this process would introduce detectable errors. Practical implementations already exist. China operates a 4,600 km integrated quantum network, and Europe’s EuroQCI initiative is actively building continent-wide infrastructure. However, a full quantum internet remains impossible without solving two major engineering challenges: quantum repeaters and quantum memory, the latter not yet able to store quantum states long enough and efficiently enough for cross-continental communication. This article reviews the roadmap of quantum network infrastructure against its theoretical potential, framing quantum memory as the central bottleneck separating operational QKD from a complete quantum internet.

**Key words:** quantum computers, quantum networking, quantum key distribution, quantum internet, entanglement, quantum memory, quantum repeaters.

**Sections:** Introduction · What Is a Quantum Computer? · Quantum Entanglement · Quantum Key Distribution · Current Infrastructure · Quantum Repeaters · Quantum Memory · Conclusions

## Qiskit project

An operational Python experiment using the Qiskit SDK and a local simulator to demonstrate the BB84 protocol for quantum key distribution.


## Code Overview

- encode_messages(bits, bases):
Encodes a random sequence of bits into quantum circuits using either the Z or X basis.

- measure_message(message, bases):
Simulates Bob’s measurement of the qubits. Applies a Hadamard gate for X-basis measurements.

- remove_trash(a_bases, b_bases, bits):
Filters out bits where Alice and Bob used mismatched bases, producing the final sifted key.

The script generates random bits and bases for both Alice and Bob, encodes each qubit accordingly, executes the circuits locally, and prints the sifted keys.

## Output 

Running BB84 on Qiskit's local simulator:
Initial values:
Alice's bits: [1 1 1 0]
Alice's bases: [0 0 0 0]
Bob's bases: [0 1 1 1]
Bob's results: [1, 1, 1, 0]

Generated keys:
Alice's key: [np.int64(1)]
Bob's key: [1]

Success: keys match

Local simulator job ID: 46010c7d-e77e-4d8e-ad8a-da9f61680b04

Full circuit:
     ┌───┐ ░ ┌─┐              
q_0: ┤ X ├─░─┤M├──────────────
     ├───┤ ░ └╥┘┌───┐┌─┐      
q_1: ┤ X ├─░──╫─┤ H ├┤M├──────
     ├───┤ ░  ║ ├───┤└╥┘┌─┐   
q_2: ┤ X ├─░──╫─┤ H ├─╫─┤M├───
     └───┘ ░  ║ ├───┤ ║ └╥┘┌─┐
q_3: ──────░──╫─┤ H ├─╫──╫─┤M├
           ░  ║ └───┘ ║  ║ └╥┘
c: 4/═════════╩═══════╩══╩══╩═
              0       1  2  3 