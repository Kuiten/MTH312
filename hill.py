import math
import numpy as np
import sympy as sp

def main():
    #67 letter alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,!?'
    #matrix to muliply message by
    matrix = sp.Matrix([[3, 7], [9, 5]])
    #size of aplhabet
    m = len(alphabet)
    #message to encrypt
    message = input('Enter your message: ')
    if(len(message) % 2 != 0):
        print("message is of odd length, adding a 'space' to the end for ease of encryption")
        message += " "
    #store encoded message
    encode = sp.Matrix([alphabet.index(i) for i in message])
    #reshape matrix to be able to muliply 
    a,b = len(message)//2,2
    shaped_encode = encode.reshape(a,b).T
    print(f'\nEncoded Message\n{shaped_encode}')
    #encrypt the message
    encrypted = matrix @ shaped_encode % m
    print(f'\nEncrypted Message\n{encrypted}')
    encrypted_message = ''
    #Convert encrypted message into letters
    for i in list(encrypted.T.reshape(1,len(message))):
        encrypted_message += alphabet[i]
    print(f'\nEncrypted Message converted to letters\n{encrypted_message}')
    #find determinant of the matrix
    determinant = matrix.det() % m
    print(f'\nDeterminant of the matrix\n{determinant}')
    #find mul. inverse of determinant mod 67
    inverse = sp.invert(determinant, m)
    print(f'\ninverse of determinant mod 67\n{inverse}')
    #calculate adjugate matrix
    adjugate_matrix = matrix.adjugate() % m
    print(f'\nadjugate matrix\n{adjugate_matrix}')
    #calculate inverse matrix
    inverse_matrix = inverse * adjugate_matrix % m
    print(f'\ninverse matrix\n{inverse_matrix}')
    #decrypt the message
    decrypted = inverse_matrix @ encrypted % m
    print(f'\nDecrypted matrix\n{decrypted}')
    #convert decrypted message into letters
    decrypted_message = ''
    for i in list(decrypted.T.reshape(1,len(decrypted))):
        decrypted_message += alphabet[i]
    print(f'\nDecryted message\n{decrypted_message}')

if __name__ == "__main__":
	main()
