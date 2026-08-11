#!/usr/bin/env python3
import base64

def solve():
    # Target array from challenge
    arr = [120, 40, 12, 239, 206, 3, 85, 112, 42, 208, 251, 86, 120, 29, 46, 226, 245, 2, 21, 50, 3, 169, 149, 0, 104, 158, 209, 29, 33, 75, 126, 212, 251, 29, 11, 71, 125, 159, 173, 9, 8, 118, 4, 215, 213, 84, 15, 24]
    
    # Key used in XOR operations
    x = [0x21, 0x45, 0x67, 0x98, 0xAD, 0x30]
    
    n = len(arr)
    half = n // 2
    c_enc = arr[:half]
    d_enc = arr[half:]
    
    # Reverse the first half (fi logic)
    # Original: z.append(ord(c[i]) ^ x[i%6])
    c_orig = ""
    for i in range(len(c_enc)):
        c_orig += chr(c_enc[i] ^ x[i % 6])
        
    # Reverse the second half (se logic)
    # Original:
    # j=0
    # for i in range(len(d)):
    #     j-=1
    #     z.append(ord(d[i]) ^ x[j])
    #     if j == -6:
    #         j = 0
    d_orig = ""
    j = 0
    for i in range(len(d_enc)):
        j -= 1
        d_orig += chr(d_enc[i] ^ x[j])
        if j == -6:
            j = 0
            
    # Combine halves to get base64 string
    base64_str = c_orig + d_orig
    print(f"[*] Reconstructed Base64: {base64_str}")
    
    # Decode base64 to get original flag
    try:
        flag = base64.b64decode(base64_str).decode('utf-8')
        print(f"[+] Verified Flag: {flag}")
    except Exception as e:
        print(f"[-] Failed to decode base64: {e}")

if __name__ == "__main__":
    solve()
