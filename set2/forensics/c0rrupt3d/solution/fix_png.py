import struct
import os

def fix_png(input_path, output_path):
    with open(input_path, 'rb') as f:
        data = f.read()

    # PNG Header: 89 50 4E 47 0D 0A 1A 0A
    png_header = b'\x89PNG\r\n\x1a\n'
    
    # The current file starts with 8 null bytes
    # 00000000000000000000000d49484452
    # The '0000000d' (length of IHDR) starts at index 8
    
    fixed_data = png_header + data[8:]
    
    # Fix IEND chunk (last 12 bytes)
    # Length: 00 00 00 00
    # Type: 49 45 4E 44 (IEND)
    # CRC: AE 42 60 82
    iend_chunk = b'\x00\x00\x00\x00IEND\xaeB`\x82'
    fixed_data = fixed_data[:-12] + iend_chunk
    
    with open(output_path, 'wb') as f:
        f.write(fixed_data)
    
    print(f"[+] Fixed header saved to {output_path}")

def analyze_chunks(path):
    print(f"[*] Analyzing chunks of {path}...")
    with open(path, "rb") as f:
        header = f.read(8)
        if header != b"\x89PNG\r\n\x1a\n":
            print("[-] Invalid PNG header")
            return
        
        while True:
            chunk_header = f.read(8)
            if len(chunk_header) < 8:
                break
            length, chunk_type = struct.unpack(">I4s", chunk_header)
            data = f.read(length)
            crc = f.read(4)
            
            # Check for common corrupted chunk names
            try:
                type_str = chunk_type.decode()
            except:
                type_str = str(chunk_type)
            
            print(f"  Found chunk {type_str} of length {length}")
            
            # Check CRC
            import zlib
            calculated_crc = zlib.crc32(chunk_type + data) & 0xffffffff
            stored_crc = struct.unpack(">I", crc)[0]
            if calculated_crc != stored_crc:
                print(f"    [!] CRC Mismatch! Calculated: {hex(calculated_crc)}, Stored: {hex(stored_crc)}")
            
            if chunk_type == b"IEND":
                break

if __name__ == "__main__":
    input_file = "/home/ubuntu/set2/forensics/c0rrupt3d/challenge/flag.png"
    output_file = "/home/ubuntu/set2/forensics/c0rrupt3d/challenge/fixed_flag.png"
    fix_png(input_file, output_file)
    analyze_chunks(output_file)
