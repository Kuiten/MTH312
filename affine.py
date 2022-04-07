import math
import numpy as np
import sympy as sp

def main():
     #Alphabet for the cipher
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    #shift amounts
    mshift = int(input('Enter your desired multiplaction shift amount: '))
    ashift = int(input('\nEnter your desired additive shift amount: '))
    #hold encoded message(numbers)
    encoded = []
    #hold encrypted message(numbers)
    encrypted = []
    #holds the encrypted message(letters)
    encrypted_message = ''
    #if mshift is  or less exit
    if mshift <= 0:
        print("multiplicative shift cannot be 0 or less")
        quit()
    #verify mshift has a mult inverse
    while math.gcd(mshift, 26) != 1:
        print("\nRequested multiplicative shift does not have a multiplicative inverse mod 26")
        mshift = int(input('Enter a new multiplaction shift amount(Hint: gcf with 26 must be 1): '))
    #get message froom user, conver to all lowercase
    message = input('Enter your message: ')
    message = message.lower()
    #remove spaces from message
    message = message.replace(" ", "")
    #encode the message
    for j in range(len(message)):
        encoded.append(alphabet.index(message[j]))
    print(f'Message once encoded: {encoded}\n')
    #encrypt the message
    for i in encoded:
        encrypted.append(((mshift*i)+ashift) % 26) 
    print(f'Message once encrypted: {encrypted}\n')
    #convert to letters
    for i in encrypted:
        encrypted_message += alphabet[i]
    print(f'Encrypted message with no spaces: {encrypted_message}\n')
    #find mult. inverse
    m_inverse = sp.invert(mshift, 26)
    decrypted = []
    #decrypt the message
    for i in encrypted:
        decrypted.append(((i - ashift) * m_inverse) % 26)
    print(f'Decrpyting Message: {decrypted}\n')
    decrypted_message = ''
    #convert back to letters
    for i in decrypted:
        decrypted_message += alphabet[i]
    print(f'Decrypted message with no spaces: {decrypted_message}\n')
if __name__ == "__main__":
	main()
    
