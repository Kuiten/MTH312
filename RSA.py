import math
import random
import numpy as np
import sympy as sp


def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(num/2)+1):
        if num % i == 0:
            return False
    return True

def main():
    #primes to use during encryption
    p = int(input("Please enter your first prime p: "))
    q = int(input("Please enter your second prime q: "))
    if not is_prime(p):
        print("p is not prime cannot encrypt")
        return
    if not is_prime(q):
        print("q is not prime cannot encrypt")
        return
    #both primes multiplied by each other(this is our modulus)
    mod = p * q
    #this is phi, used to verify d
    phi = (p-1)*(q-1)
    #choose random number such that 1 < d < phi - 1
    d = random.randint(2, phi-2)
    while math.gcd(d,phi) != 1:
        d = random.randint(2, phi-2)
    #find the value of e(mult inverse of d mod phi)
    e = int(sp.invert(d, phi))
    if e*d % phi != 1:
        print("e*d % phi should be 1, but isn't, cannot continue")
        return
    print(f"\nModulus(public): {mod}")
    print(f"e(public): {e}")
    print(f"Phi(private): {phi}")
    print(f"d(private): {d}")
    #our message
    m = int(input("\nPlease enter an integer as your message: "))
    #encrypt
    n = pow(m,e,mod)
    print(f"Encrypted message: {n}")
    #decrypt
    c = pow(n,d,mod)
    print(f"Decrypted message: {c}")
if __name__ == "__main__":
	main()
