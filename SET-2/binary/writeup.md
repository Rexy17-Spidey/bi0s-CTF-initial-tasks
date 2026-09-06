# Binary Exploitation Writeup

## Vulnerability

The program has a 64-byte stack buffer and reads input with `gets()`, so the input is not length checked. A stack value named `check` is stored next to the buffer and is later tested with `if(check) win();`.

## Exploitation

The overflow reaches `check` after 76 bytes. Supplying 76 padding bytes followed by a non-zero integer value changes `check` and reaches `win()`.

Example payload:

```python
b"A" * 76 + b"B" * 4
```

The challenge was exercised against the supplied `bof` binary and produced the flag:

`bi0s{w3lc0me_to_0v3rfl0wing_buff3rs}`
