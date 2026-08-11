# Challenge: c0rrupt3d — PNG Forensics

## Category
Forensics

## Objective
Analyze a corrupted PNG file, identify the structural errors, and repair the file to recover the flag.

## Files / Target
- `challenge/flag.png`: Corrupted PNG file.

## Enumeration
1. Inspected the hex dump of `flag.png` and found that the first 8 bytes (PNG header) were overwritten with null bytes.
2. Analyzed the end of the file and found that the `IEND` chunk was also overwritten with null bytes.
3. Verified the internal chunk structure using a custom Python script.

## Tools Used
- `python3` (struct, zlib)

## Commands
```bash
python3 fix_png.py
```

## Solution Methodology
1. **Header Repair**: Replaced the first 8 bytes with the standard PNG magic header: `\x89PNG\r\n\x1a\n`.
2. **Footer Repair**: Replaced the last 12 bytes with the standard `IEND` chunk: `\x00\x00\x00\x00IEND\xaeB`g\x82`.
3. **Verification**: Successfully opened the repaired image to reveal the flag.

## Verified Result
- **Flag**: `vidyutctf{4r3_y4_w1nn1ng_s0n?}`
- **Evidence**: Fixed image saved in `challenge/fixed_flag.png` and log in `evidence/solve_log.txt`.
