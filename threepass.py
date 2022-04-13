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
    p = int(input("Enter the prime for both 'Alice' and 'Bob' to use: "))
    message = int(input("Enter an integer as your message(less than your prime - 1): "))
    if not is_prime(p):
        print("p is not prime, cannot do the three pass protocol")
        return
    if message >= p-1:
        print("Message is not less than p-1")
        return
    #calculate e's
    alice_e = random.randint(1, p-2)
    bob_e = random.randint(1, p-2)
    while math.gcd(alice_e, p-1) != 1 or math.gcd(bob_e, p-1) != 1:
        alice_e = random.randint(1, p-2)
        bob_e = random.randint(1, p-2)
    #get d value for alice and bob
    alice_d = int(sp.invert(alice_e, p-1))
    bob_d = int(sp.invert(bob_e, p-1))
    #Alice's Encryption
    alice_n = pow(message, alice_e, p)
    print(f"Alice's Encrpytion: {alice_n}")
    #Bob's Encryption
    bob_n = pow(alice_n, bob_e, p)
    print(f"Bob's Encryption: {bob_n}")
    #Alice's Decryption
    alice_c = pow(bob_n, alice_d, p)
    print(f"Alice's Decrpytion: {alice_c}")
    #Bob's Decryption
    bob_c = pow(alice_c, bob_d, p)
    print(f"Bob's Decrpytion: {bob_c}")
    
if __name__ == "__main__":
	main()
