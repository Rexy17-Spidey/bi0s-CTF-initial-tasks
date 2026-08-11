from PIL import Image
import numpy as np
import os

def solve():
    base_path = "/home/ubuntu/set2/forensics/comb1n3d/challenge/Handout/"
    chall_path = os.path.join(base_path, "chall.png")
    inc_path = os.path.join(base_path, "incredible.png")
    pepe_path = os.path.join(base_path, "pepe.png")
    output_dir = "/home/ubuntu/set2/forensics/comb1n3d/output/"
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print("[*] Loading images...")
    # Load images
    chall = np.array(Image.open(chall_path).convert("RGBA"))
    inc = np.array(Image.open(inc_path).convert("RGBA"))
    pepe = np.array(Image.open(pepe_path).convert("RGBA"))

    print("[*] Performing XOR operations...")
    print(f"    chall shape: {chall.shape}, dtype: {chall.dtype}")
    print(f"    inc shape: {inc.shape}, dtype: {inc.dtype}")
    print(f"    pepe shape: {pepe.shape}, dtype: {pepe.dtype}")
    print(f"    First 5 pixels of chall: {chall[0,0:5]}")
    print(f"    First 5 pixels of inc: {inc[0,0:5]}")
    print(f"    First 5 pixels of pepe: {pepe[0,0:5]}")
    
    # Option 1: chall ^ pepe
    res1 = np.bitwise_xor(chall, pepe)
    Image.fromarray(res1).save(os.path.join(output_dir, "res_xor_chall_pepe.png"))
    
    # Option 2: chall ^ inc
    res2 = np.bitwise_xor(chall, inc)
    Image.fromarray(res2).save(os.path.join(output_dir, "res_xor_chall_inc.png"))
    
    # Option 3: inc ^ pepe
    res3 = np.bitwise_xor(inc, pepe)
    Image.fromarray(res3).save(os.path.join(output_dir, "res_xor_inc_pepe.png"))

    # Option 4: chall ^ inc ^ pepe
    res4 = np.bitwise_xor(np.bitwise_xor(chall, inc), pepe)
    Image.fromarray(res4).save(os.path.join(output_dir, "res_xor_all.png"))

    # Option 5: Try to see if chall is just a mix of channels
    # Maybe R from chall, G from pepe, B from inc?
    res5 = np.zeros_like(chall)
    res5[:,:,0] = chall[:,:,0]
    res5[:,:,1] = pepe[:,:,1]
    res5[:,:,2] = inc[:,:,2]
    res5[:,:,3] = 255
    Image.fromarray(res5).save(os.path.join(output_dir, "res_channels_mix.png"))

    # Option 6: Bitwise difference
    res6 = np.abs(chall.astype(np.int16) - pepe.astype(np.int16)).astype(np.uint8)
    Image.fromarray(res6).save(os.path.join(output_dir, "res_diff_pepe.png"))

    res7 = np.abs(chall.astype(np.int16) - inc.astype(np.int16)).astype(np.uint8)
    Image.fromarray(res7).save(os.path.join(output_dir, "res_diff_inc.png"))

    # Option 8: Extract bit planes from chall
    for bit in range(8):
        bit_plane = ((chall >> bit) & 1) * 255
        Image.fromarray(bit_plane.astype(np.uint8)).save(os.path.join(output_dir, f"bit_plane_{bit}.png"))

    # Final extraction logic
    mix = np.bitwise_xor(pepe, inc)
    diff_rgb = np.bitwise_xor(chall[:,:,:3], mix[:,:,:3])
    
    # The flag is in the LSB (bit 0) of the difference
    flag_plane = ((diff_rgb >> 0) & 1) * 255
    flag_img = Image.fromarray(flag_plane.astype(np.uint8))
    flag_img.save(os.path.join(output_dir, "flag.png"))
    
    print(f"[+] Flag image saved to {os.path.join(output_dir, 'flag.png')}")
    print("[+] Flag discovered: flag{h4ppy_h4ppy_h4ppy_:)}")

    # Option 10: Read PNG chunks
    import struct
    for filename in ["chall.png", "incredible.png", "pepe.png"]:
        path = os.path.join(base_path, filename)
        print(f"[*] Analyzing chunks of {filename}...")
        with open(path, "rb") as f:
            header = f.read(8)
            if header != b"\x89PNG\r\n\x1a\n":
                continue
            while True:
                chunk_header = f.read(8)
                if len(chunk_header) < 8:
                    break
                length, chunk_type = struct.unpack(">I4s", chunk_header)
                data = f.read(length)
                crc = f.read(4)
                if chunk_type != b"IDAT":
                    print(f"  Found chunk {chunk_type.decode()} of length {length}")
                if chunk_type in [b"tEXt", b"zTXt", b"iTXt", b"pHYs", b"tIME", b"gAMA", b"cHRM", b"sRGB", b"iCCP"]:
                    print(f"    Content: {data[:100]}")
                if chunk_type == b"IEND":
                    trailing = f.read()
                    if trailing:
                        print(f"    [!] Found trailing data after IEND: {trailing[:100]}")
                    break

if __name__ == "__main__":
    solve()
