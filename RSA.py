import math
import numpy as np
import sympy as sp

def main():
    #primes to use during encryption
    p = 31
    q = 197
    #both primes multiplied by each other(this is our modulus)
    mod = p * q
    #this is phi, used to verify d
    phi = (p-1)*(q-1)
    d = 11
    if math.gcd(d,phi) != 1:
        print("d does not have a mult. inverse please try a new value of d")
        return
    #find the value of e(mult inverse of d mod phi)
    e = sp.invert(d, phi)
    if e*d % phi != 1:
        print("e*d % phi should be 1, but isn't, cannot continue")
        return
    #our message
    m = 4211






if __name__ == "__main__":
	main()
