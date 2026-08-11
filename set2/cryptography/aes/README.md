# Challenge: AES Cryptography

## Category
Cryptography

## Objective
Analyze symmetric AES encryption configuration (key, IV/nonce, mode of operation, padding) and decrypt the ciphertext to recover the flag.

## Files / Target
- Supplied source code or cryptographic parameters file.

## Enumeration
1. Inspect encryption script or configuration files.
2. Identify AES mode (CBC, ECB, CTR, GCM) and block padding scheme (PKCS7).
3. Check key and IV generation mechanisms (weak random seeds, hardcoded keys, ECB ECB pattern leaks, or IV reuse in CBC/GCM).

## Tools Used
- Python (`pycryptodome` / `cryptography`)
- `xxd`, `hexdump`

## Commands
```python
from Crypto.Cipher import AES
```

## Solution Methodology
1. Extract key, IV, mode, and ciphertext from challenge sources.
2. Construct the appropriate AES cipher object.
3. Decrypt ciphertext and unpad/decode to recover plaintext flag.

## Verified Result
- **Flag**: Pending challenge parameters.
- **Evidence**: Stored in `evidence/aes_analysis.txt`.
