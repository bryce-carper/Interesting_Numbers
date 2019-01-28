# Some function definitions that apply to my major.

def plist(k): # Generate list of primes less than or equal to k
    plist = []
    for i in range(k - 1):
        comp = 0
        for p in plist:
            if ((i + 2) % p) == 0:
                comp = 1
                break
        if comp == 0:
            plist.append(i + 2)
    return plist

def tlist(k): # Generate list of triangulars less than or equal to k
    tlist = [1]
    i = 2
    while (tlist[-1] + i) <= k:
        tlist.append(tlist[-1] + i)
        i += 1
    return tlist

def slist(k): # Generate list of squares less than or equal to k
    slist = [1]
    i = 2
    while (slist[-1] + (2 * i - 1)) <= k:
        slist.append((slist[-1] + (2 * i - 1)))
        i += 1
    return slist

def flist(k): # Generate list of factorials less than or equal to k
    flist = [1]
    i = 2
    while (flist[-1] * i) <= k:
        flist.append(flist[-1] * i)
        i += 1
    return flist

# A program to examine some interesting numbers

print("We will inductively determine which positive integers are interesting!")

k = int(input("Up through what positive integer should we check? \nk = "))

p = plist(k)
t = tlist(k)
s = slist(k)
f = flist(k)
print()
for i in range(k):
    descriptor = "is"
    if ((i+1) in p):
        descriptor += " a prime number,"
    if ((i+1) in t):
        descriptor += " a triangular number,"
    if ((i+1) in s):
        descriptor += " a square number,"
    if ((i+1) in f):
        descriptor += " a factorial number,"
    if descriptor == "is":
        descriptor = "would be the first non-interesting number,"
    print((i + 1), descriptor, "and so is an interesting number as a result!\n")
print("All done! Wow, those were some interesting integers!")
