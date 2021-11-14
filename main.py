import numpy as np
import random

def partition_coordinates(s, n):
    I = {}
    for i in range(n):
        b = random.randint(0, s)
        if b not in I:
            I[b] = []
        I[b].append(i)
    return I

def binary_search(I, f, x, z):
    if len(I) == 1:
        return I
    t = len(I) // 2
    indices = np.intersect1d(np.where(x != z), np.concatenate(I[:t]))
    x_prime = x.copy()
    x_prime[indices] = z[indices]

    if f(x) != f(x_prime):
        return binary_search(I[:t], f, x, x_prime)
    return binary_search(I[t:], f, x_prime, z)

def Junta(f, k, eps, n, s, r):
    relavants = []
    l = 0
    I = list(partition_coordinates(s, n).values())
    print("parts ",len(I))
    S = I.copy()
    for _ in range(int(r)):
        x, y = sample(n),sample(n)
        z = x.copy()
        indices = np.concatenate(S)
        z[indices] = y[indices]
        if f(x) != f(z):
            part = binary_search(S, f, x, z)[0]
            relavants.append(part)
            if len(relavants) % 10 == 0:
                print(len(relavants)," in ",_)
            S.remove(part)
            l += 1
            if l > k:
                print("NOT ",k,"-JUNTA")
                return relavants
    print(k,"-JUNTA")
    return relavants
