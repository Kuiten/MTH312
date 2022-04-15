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
    #choose random prime
    p = random.randint(3, 1000000)
    while not is_prime(p):
        p = random.randint(3, 1000000)
    #random generator 
    g = random.randint(2, 1000000)
    #random secret number b such that 1 < b < p
    b = random.randint(2, p-1)
    #public B to be shared
    B = pow(g, b, p)
    print(f"Bob's public key(p,g,b): {p}, {g}, {B}")
    #Message
    m = int(input("\nEnter a number as your message: "))
    #r value
    r = int(input("Enter a random number r, such that 1 < r < p: "))
    while r < 1 or r > p:
        print("r was not in valid range try again")
        r = int(input("Enter a random number r, such that 1 < r < p: "))
    #calculate nonce (R)
    nonce = pow(g, r, p)
    #encrypt message(alice)
    encrypted = (m * pow(B, r, p)) % p
    print(f"\nnonce = {nonce}")
    print(f"Encrypted Message(n) = {encrypted}")
    #decrpyt message(bob)
    decrypt = (encrypted * pow(nonce, p-1-b, p)) % p
    print(f"decrypted message: {decrypt}")
if __name__ == "__main__":
	main()
