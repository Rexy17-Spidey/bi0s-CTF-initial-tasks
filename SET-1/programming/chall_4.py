s = input().strip()

frequency = {}

for ch in s:
    if ch not in frequency:
        frequency[ch] = 1
    else:
        frequency[ch] += 1

for ch, count in frequency.items():
    print(f"{ch}: {count}")

print("Reversed string:", s[::-1])