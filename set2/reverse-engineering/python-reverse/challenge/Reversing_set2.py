import base64

arr = [120, 40, 12, 239, 206, 3, 85, 112, 42, 208, 251, 86, 120, 29, 46, 226, 245, 2, 21, 50, 3, 169, 149, 0, 104, 158, 209, 29, 33, 75, 126, 212, 251, 29, 11, 71, 125, 159, 173, 9, 8, 118, 4, 215, 213, 84, 15, 24]
x = [0x21, 0x45, 0x67, 0x98, 0xAD, 0x30]
z = []

def fi(n, a):
    return a[:n//2]

def se(n, a):
    return a[n//2:]

def f(a):
    b = base64.b64encode(a.encode('utf-8'))
    return b.decode('utf-8')

def d(a):
    global x, z
    n = len(a)
    c = fi(n,a)
    d = se(n,a)
    for i in range(len(c)):
        z.append(ord(c[i]) ^ x[i%6])
    j=0
    for i in range(len(d)):
        j-=1
        z.append(ord(d[i]) ^ x[j])
        if j == -6:
            j = 0
    return z

def main():
    global arr
    a = input("Enter Flag: ")
    e = f(a)
    g = d(e)
    if g == arr:
        print("You got it!")
    else:
        print("Nope!")


if __name__ == "__main__":
    main()
