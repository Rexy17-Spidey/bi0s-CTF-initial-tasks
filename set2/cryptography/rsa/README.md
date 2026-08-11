# Challenge: RSA Cryptography

## Category
Cryptography

## Objective
Analyze asymmetric RSA encryption parameters, identify mathematical weaknesses (such as small modulus $n$, weak prime generation, or low public exponent $e$), and recover the plaintext flag.

## Files / Target
- Supplied parameters file (public key, modulus $n$, exponent $e$, ciphertext $c$)

## Enumeration
1. Inspect public parameters ($n, e, c$).
2. Check modulus length (e.g., bit size).
3. Test for common vulnerabilities:
   - Small $n$ vulnerable to direct integer factorization (`factordb` or trial division).
   - Hastad's Broadcast Attack (small $e$ with multiple ciphertexts).
   - Wiener's Attack (small private exponent $d$).
   - Common modulus attack.

## Tools Used
- Python (`gmpy2`, `Crypto.PublicKey`, `factordb-py`)
- SageMath (if applicable)

## Commands
```python
# Factorization check or parameter loading
```

## Solution Methodology
1. Extract parameters from challenge files.
2. Factor $n$ into primes $p$ and $q$.
3. Compute Euler's totient $\phi(n) = (p-1)(q-1)$.
4. Compute private exponent $d = e^{-1} \pmod{\phi(n)}$.
5. Decrypt ciphertext $m = c^d \pmod n$ and decode to ASCII string.

## Verified Result
- **Flag**: Pending parameter file provision.
- **Evidence**: Stored in `evidence/rsa_analysis.txt`.
