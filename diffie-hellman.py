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
    #prime
    p = int(input("Please eneter you agreed upon prime(p): "))
    if not is_prime(p):
        print("ERROR: agreed upon prime(p) is not prime")
        return
    #generator
    g = int(input("Please enter your agreed upon generator(g): "))
    #alice's secret number
    a = random.randint(2, 100)
    #alice's number sent to Bob
    A = pow(g, a, p)
    print(f"Alices value sent to Bob A = {A}")
    # bob's secret number
    b = random.randint(2, 100)
    #Bob's number sent to Alice
    B = pow(g, b, p)
    print(f"Bobs values sent to Alice B = {B}")
    #Key calculated by Alice
    KA = pow(B, a, p)
    #key calculated by Bob
    KB = pow(A, b, p)
    #Both keys should be equal, this is used for encryption
    if KA != KB:
        print("ERROR: Bobs key and Alices key are not equal")
        return
    print(f"Shared key = {KA}")
if __name__ == "__main__":
	main()
