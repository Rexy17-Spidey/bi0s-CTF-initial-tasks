# Challenge: Python Reverse Engineering

## Category
Reverse Engineering

## Objective
Reverse the provided Python script to understand the validation transformation and recover the correct flag.

## Files / Target
- `challenge/Reversing_set2.py`: The original challenge script.

## Enumeration
1. **File Type**: Identified as a Python 3 source file.
2. **Logic Analysis**:
   - Input flag is first Base64 encoded.
   - The Base64 string is split into two halves (`fi` and `se`).
   - The first half is XORed with a key `x = [0x21, 0x45, 0x67, 0x98, 0xAD, 0x30]` using forward indexing (`i % 6`).
   - The second half is XORed with the same key using reverse indexing (`-1` to `-6`).
   - The result is compared against a hardcoded integer array `arr`.

## Tools Used
- `python3`
- `base64` library

## Commands
```bash
# Execute the solver
python3 solution/solve.py
```

## Solution Methodology
1. **Inverse XOR**: Created a solver script that iterates through the target `arr`, applying the XOR key in the same forward and reverse patterns to recover the Base64 characters.
2. **Base64 Decoding**: Reconstructed the full Base64 string and decoded it to reveal the plaintext flag.

## Verified Result
- **Flag**: `bi0s{y0u_ar3_n0w_4_r3v3rs3_3ng1n33r}`
- **Evidence**: Stored in `evidence/execution_log.txt`.
