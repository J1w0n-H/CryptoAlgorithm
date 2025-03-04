import numpy as np

UID = 121326492                                        #Your UID should be included in your program as a global variable
Last_Name = 'Hwang'                      #Your Last Name should be included in your program as a global variable
First_Name = 'Jiwon'                    #Your First Name should be included in your program as a global variable

def caesar_str_enc(plaintext, k):
    plaintext = plaintext.replace(" ", "")  # Remove spaces from the plaintext
    plaintext = plaintext.upper()  # Convert the plaintext to uppercase
    ciphertext = ""  # Initialize ciphertext

    for i in range(len(plaintext)):  # Encrypt the plaintext using the Caesar cipher with key k
        ciphertext += chr((ord(plaintext[i]) - 65 + k) % 26 + 65)
    return ciphertext                  #Your function must return a string

def caesar_str_dec(ciphertext, k):                #Your decryption function should have the same name and must accept a string as the first argument and an integer as a second argument
    ciphertext = ciphertext.replace(" ", "")  # Remove spaces from the ciphertext
    ciphertext = ciphertext.upper()  # Convert the ciphertext to uppercase
    plaintext = ""  # Initialize plaintext
    length = len(ciphertext)
    for i in range(length):                         #Decrypt the ciphertext using the Caesar cipher with key k
        plaintext += chr((ord(ciphertext[i]) - 65 - k) % 26 + 65)
    return plaintext                          #Your function must return a string

def vigenere_enc(keyword, plaintext):
    # plaintext is the plaintext string of arbitrary length
    # Both strings will be from {a,b,...,z,A,B,...,Z} and you need to convert to upper case
    keyword = keyword.upper()

    # Repeat the keyword to match the length of the plaintext
    if len(plaintext) > len(keyword):
        for i in range(len(plaintext) - len(keyword)):
            keyword += keyword[i % len(keyword)]
    ciphertext = ""
    for i in range(len(plaintext)):
        k=ord(keyword[i]) - 65
        ciphertext+=caesar_str_enc(plaintext[i], k)
    return ciphertext


def vigenere_dec(keyword, ciphertext): 
    # ciphertext is the ciphertext string of arbitrary length
    # Both strings will be from {a,b,...,z,A,B,...,Z}
    keyword = keyword.upper()
    # Repeat the keyword to match the length of the ciphertext
    if len(ciphertext) > len(keyword):
        for i in range(len(ciphertext) - len(keyword)):
            keyword += keyword[i % len(keyword)]

    
    plaintext = ""  # Initialize plaintext
    for i in range(len(ciphertext)):
        k = ord(keyword[i]) - 65
        plaintext += chr((ord(ciphertext[i]) - 65 - k) % 26 + 65)
    # perform the decryption of given ciphertext using the given keyword
    # according to the Vigenere cipher. You need to repeat the keyword
    # enough times if needed to make it the same length as ciphertext

    return plaintext


print(caesar_str_enc('A TEST SENTENCE',2),caesar_str_dec('CVGUVUGPVG',2),vigenere_enc('KEY', 'Test String'),vigenere_dec('KEY', 'DIQDWRBMLQ'))

