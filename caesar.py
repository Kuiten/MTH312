import numpy as np

def main():
    #Alphabet for the cipher
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    #get message froom user, conver to all lowercase
    message = input('Enter your message: ')
    message = message.lower()
    #remove spaces from message
    message = message.replace(" ", "")
    #hold encoded message(numbers)
    encoded = []
    #hold encrypted message(numbers)
    encrypted = []
    #holds the encrypted message(letters)
    encrypted_message = ''
    #encode the message
    for j in range(len(message)):
        encoded.append(alphabet.index(message[j]))
    print(f'Message once encoded: {encoded}\n')
    #encrypt the message
    for i in encoded:
        encrypted.append((i+3) % 26) 
    print(f'Message once encrypted: {encrypted}\n')
    for i in encrypted:
        encrypted_message += alphabet[i]
    print(f'Encrypted message with no spaces: {encrypted_message}\n')
if __name__ == "__main__":
	main()
