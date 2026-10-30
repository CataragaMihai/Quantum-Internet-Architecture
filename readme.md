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

## Requirements

- Python 3
- Qiskit
- NumPy

Install the required Python packages with:

```bash
pip install qiskit numpy
```

## Code Overview

- encode_messages(bits, bases):
Encodes a random sequence of bits into quantum circuits using either the Z or X basis.

- measure_message(circuits, bases):
Simulates Bob’s measurement of the qubits. Applies a Hadamard gate for X-basis measurements.

- remove_trash(a_bases, b_bases, bits):
Filters out bits where Alice and Bob used mismatched bases, producing the final sifted key.

The script generates random bits and bases for both Alice and Bob, encodes each qubit accordingly, executes the circuits locally, and prints the sifted keys.

## Output

```text
Running BB84 on Qiskit's local simulator:
Initial values:
Alice's bits: [1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]
Alice's bases: [1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0]
Bob's bases: [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
Bob's results: [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1]

Generated keys:
Alice's key: [1, 0, 0, 0, 0, 1, 1, 1]
Bob's key: [1, 0, 0, 0, 0, 1, 1, 1]

Success: keys match

Local simulator job ID: 5dc2ea87-52d0-4095-bbe3-f64cdb25e542

Full circuit:
      ┌───┐┌───┐ ░ ┌─┐                                                      
 q_0: ┤ X ├┤ H ├─░─┤M├──────────────────────────────────────────────────────
      ├───┤├───┤ ░ └╥┘┌───┐                                  ┌─┐            
 q_1: ┤ X ├┤ H ├─░──╫─┤ H ├──────────────────────────────────┤M├────────────
      ├───┤├───┤ ░  ║ └┬─┬┘                                  └╥┘            
 q_2: ┤ X ├┤ H ├─░──╫──┤M├────────────────────────────────────╫─────────────
      ├───┤└───┘ ░  ║  └╥┘ ┌───┐                              ║ ┌─┐         
 q_3: ┤ H ├──────░──╫───╫──┤ H ├──────────────────────────────╫─┤M├─────────
      └───┘      ░  ║   ║  └┬─┬┘                              ║ └╥┘         
 q_4: ───────────░──╫───╫───┤M├───────────────────────────────╫──╫──────────
      ┌───┐      ░  ║   ║   └╥┘ ┌─┐                           ║  ║          
 q_5: ┤ H ├──────░──╫───╫────╫──┤M├───────────────────────────╫──╫──────────
      ├───┤      ░  ║   ║    ║  └╥┘┌─┐                        ║  ║          
 q_6: ┤ H ├──────░──╫───╫────╫───╫─┤M├────────────────────────╫──╫──────────
      └───┘      ░  ║   ║    ║   ║ └╥┘┌─┐                     ║  ║          
 q_7: ───────────░──╫───╫────╫───╫──╫─┤M├─────────────────────╫──╫──────────
                 ░  ║   ║    ║   ║  ║ └╥┘┌─┐                  ║  ║          
 q_8: ───────────░──╫───╫────╫───╫──╫──╫─┤M├──────────────────╫──╫──────────
      ┌───┐┌───┐ ░  ║   ║    ║   ║  ║  ║ └╥┘┌─┐               ║  ║          
 q_9: ┤ X ├┤ H ├─░──╫───╫────╫───╫──╫──╫──╫─┤M├───────────────╫──╫──────────
      ├───┤├───┤ ░  ║   ║    ║   ║  ║  ║  ║ └╥┘┌─┐            ║  ║          
q_10: ┤ X ├┤ H ├─░──╫───╫────╫───╫──╫──╫──╫──╫─┤M├────────────╫──╫──────────
      ├───┤└───┘ ░  ║   ║    ║   ║  ║  ║  ║  ║ └╥┘┌─┐         ║  ║          
q_11: ┤ X ├──────░──╫───╫────╫───╫──╫──╫──╫──╫──╫─┤M├─────────╫──╫──────────
      ├───┤┌───┐ ░  ║   ║    ║   ║  ║  ║  ║  ║  ║ └╥┘┌─┐      ║  ║          
q_12: ┤ X ├┤ H ├─░──╫───╫────╫───╫──╫──╫──╫──╫──╫──╫─┤M├──────╫──╫──────────
      ├───┤├───┤ ░  ║   ║    ║   ║  ║  ║  ║  ║  ║  ║ └╥┘┌───┐ ║  ║ ┌─┐      
q_13: ┤ X ├┤ H ├─░──╫───╫────╫───╫──╫──╫──╫──╫──╫──╫──╫─┤ H ├─╫──╫─┤M├──────
      ├───┤├───┤ ░  ║   ║    ║   ║  ║  ║  ║  ║  ║  ║  ║ ├───┤ ║  ║ └╥┘┌─┐   
q_14: ┤ X ├┤ H ├─░──╫───╫────╫───╫──╫──╫──╫──╫──╫──╫──╫─┤ H ├─╫──╫──╫─┤M├───
      ├───┤└───┘ ░  ║   ║    ║   ║  ║  ║  ║  ║  ║  ║  ║ ├───┤ ║  ║  ║ └╥┘┌─┐
q_15: ┤ X ├──────░──╫───╫────╫───╫──╫──╫──╫──╫──╫──╫──╫─┤ H ├─╫──╫──╫──╫─┤M├
      └───┘      ░  ║   ║    ║   ║  ║  ║  ║  ║  ║  ║  ║ └───┘ ║  ║  ║  ║ └╥┘
c: 16/══════════════╩═══╩════╩═══╩══╩══╩══╩══╩══╩══╩══╩═══════╩══╩══╩══╩══╩═
                    0   2    4   5  6  7  8  9  10 11 12      1  3  13 14 15
```
