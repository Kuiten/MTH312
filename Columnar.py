import math
import random
import numpy as np
import sympy as sp

def main():
    key_word = "ENCRYPT"
    message = input("Please type your message to be encrypted: ")
    message = message.lower()
    message = message.replace(" ", "")
    encrypted = dict.fromkeys(['E', 'N', 'C', 'R', 'Y', 'P', 'T'],"")
    #Encode the message
    #for key
    for key in encrypted:
        #for message
        for i in range(key_word.index(key), len(message), len(key_word)):
            encrypted[key] += message[i]
    #Encrypt the message
    encrypted_message = ""
    for key in sorted(encrypted):
        encrypted_message += encrypted[key]
    print(f"\nkey: {key_word}")
    print("Read off in columns")
    print(f"Encrypted message:\n {encrypted_message}")
if __name__ == "__main__":
	main()
