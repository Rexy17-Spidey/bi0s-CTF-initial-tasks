s = input().strip()

result = ""

for i in range(0, len(s), 2):
    pair = s[i:i+2]

    if pair == "xx":
        result += "0"
    elif pair == "ox":
        result += "1"
    elif pair == "oo":
        result += "2"

print(result)