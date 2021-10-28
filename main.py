import random
import numpy as np


def binary_search(I, f, x, z):
    if len(I) == 1:
        return I
    t = len(I) // 2
    indices = np.concatenate(t)
    x_prime = x.copy()
    x_prime[indices] = z[indices]

    if f(x) != f(x_prime):
        binary_search(I[:t], f, x, x_prime)
    binary_search(I[t:], f, x_prime, z)


def partition_coordinates(s, n):
    I = {}
    for i in range(n):
        b = random.randint(0, s)
        if b not in I:
            I[b] = []
        I[b].append(i)
    return I


def junta_test(f, k, eps, n):
    # randomly partition coordinates into s sets
    s = (10 ** 20) * (k ** 9) / (eps ** 5)
    I = partition_coordinates(s, n)
    r = 12 * (k + 1) / eps
    l = 0

    S = I.copy()
    # to be replaced with real data
    for _ in range(r):
        x, y = _
        # generate x,y
        z = x.copy()
        indices = np.concatenate(S)
        z[indices] = y[indices]

        if f(x) != f(z):
            part = binary_search(S, f, x, z)
            # remove
            S.remove(part)
            l += 1
            if l > k:
                return False
    return True


if __name__ == '__main__':
    # preprocess data
    junta_test()
