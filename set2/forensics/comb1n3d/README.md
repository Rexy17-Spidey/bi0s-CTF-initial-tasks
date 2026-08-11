# Challenge: comb1n3d — Steganography

## Category
Forensics

## Objective
Investigate the supplied challenge files for hidden steganographic payloads and build a fully reproducible Python script to extract the flag.

## Files / Target
- `challenge/Handout/chall.png`: Glitched composite image.
- `challenge/Handout/pepe.png`: Reference image 1.
- `challenge/Handout/incredible.png`: Reference image 2.

## Enumeration
1. Analyzed the three images and identified that `chall.png` appears to be a glitched version of the other two.
2. Verified that `chall.png` RGB values are mathematically related to the XOR of `pepe.png` and `incredible.png`.
3. Discovered a hidden noise layer by calculating `chall ^ (pepe ^ incredible)`.

## Tools Used
- `python3` (Pillow, NumPy)

## Commands
```bash
python3 solve.py
```

## Solution Methodology
1. **Isolate Hidden Layer**: The `chall.png` image is a composite of `pepe.png` and `incredible.png` with an additional noise layer. By XORing the two reference images and then XORing the result with the challenge image, we isolate the hidden layer.
2. **Bit Plane Analysis**: Analyzed the bit planes of the isolated layer.
3. **Extraction**: The flag is clearly visible in the Least Significant Bit (LSB) plane of the isolated difference layer.

## Verified Result
- **Flag**: `flag{h4ppy_h4ppy_h4ppy_:)}`
- **Evidence**: Flag image saved in `output/flag.png` and log in `evidence/solve_log.txt`.
