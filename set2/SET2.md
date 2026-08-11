# bi0s Recruitment Challenge: Set 2 Master Index

## Overview

This repository contains the organized submission structure, solution scripts, evidence logs, and technical writeups for **Set 2** of the bi0s recruitment challenge. In accordance with non-negotiable integrity rules, all solutions, evidence, and flags are strictly derived from verified challenge files and target infrastructure.

## Scope of Work

The focus areas for Set 2 comprise four core cybersecurity domains:
1. **Reverse Engineering**: Analyzing and reversing compiled or interpreted code logic to recover validation mechanisms and flags.
2. **Web Exploitation**: Investigating client-side access controls, hidden application components, and flag hunting across endpoints.
3. **Cryptography**: Analyzing asymmetric (RSA) and symmetric (AES) encryption parameters, key derivation, and decryption pathways.
4. **Forensics**: Performing structural file forensics (PNG chunk analysis) and steganographic extraction with reproducible solver scripts.

---

## Directory Structure and Challenge Index

| Category | Challenge Name | Status / Description | Primary Deliverables |
| :--- | :--- | :--- | :--- |
| **Reverse Engineering** | `python-reverse` | **SOLVED**: Reversed XOR/Base64 logic | `README.md`, `solution/solve.py`, `evidence/` |
| **Web Exploitation** | `flag-hunting` | **SOLVED**: Multi-component fragment hunting | `README.md`, `scripts/`, `evidence/` |
| **Web Exploitation** | `chrome-junkie` | **SOLVED**: Cookie tampering & privilege escalation | `README.md`, `scripts/`, `evidence/` |
| **Cryptography** | `rsa` | RSA parameter analysis & recovery | `README.md`, `solution/solve.py`, `evidence/` |
| **Cryptography** | `aes` | AES mode, IV, and key analysis | `README.md`, `solution/solve.py`, `evidence/` |
| **Forensics** | `comb1n3d` | **SOLVED**: Steganographic payload extraction | `README.md`, `solve.py`, `challenge/`, `output/`, `evidence/` |
| **Forensics** | `c0rrupt3d` | **SOLVED**: PNG header & IEND chunk repair | `README.md`, `solution/fix_png.py`, `evidence/` |

---

## Integrity and Verification Standard

- **No Fabricated Data**: Every command executed, hash computed, HTTP request dispatched, and flag recovered must be backed by raw evidence files stored within the respective challenge `evidence/` directories.
- **Reproducibility**: Analysis scripts (such as steganography extraction and cryptographic decryption solvers) are fully documented and executable.
- **Interview Readiness**: Each challenge writeup follows a rigorous structured format detailing enumeration steps, tools used, exact commands, vulnerability mechanics, and model interview explanations.

*Author*: Cybersecurity CTF Implementation Assistant for bi0s Recruitment
