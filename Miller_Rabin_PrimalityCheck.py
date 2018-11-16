import math
import random
import time


def powerOfTwo(n):
    r = 0
    d = n
    while(d%2==0):
        r += 1
        d >>= 1
    assert(2**r * d == n)
    return r, d

def MillerRabinTest(n, k):
    """
    Miller-Rabin primality test.
 
    A return value of False means n is certainly not prime. A return value of
    True means n is very likely a prime.
    """
    if n <= 3:
        return False
    r, d = powerOfTwo(n-1)
    for _ in range(k):
        rInt = random.randint(2, n-2)
        x = pow(rInt,d,n)
        if x == 1 or x == n - 1:
            continue
        flag = 0
        for _ in range(r-1):
            x = pow(x,2,n)
            if x == n - 1:
                flag = 1
                break
        if flag == 1:
            continue
        return False
    return True

def is_prime(n):
    '''
    Simpler primality check for time comparison
    '''
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n%2 == 0 or n%3 == 0:
        return False
    i = 5
    while (i*i <= n):
        if n%i == 0 or n%(i+2) == 0:
            return False
        i += 6

    return True


n = 200000015717
t0 = time.time()
print(MillerRabinTest(n, 8))
t1 = time.time()

print("Miller Rabin: " + str(t1-t0))

t0 = time.time()
print(is_prime(n))
t1 = time.time()

print("Simple Primality: " + str(t1-t0))
