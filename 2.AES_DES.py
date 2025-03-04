from Crypto.Cipher import AES, DES


UID = 121329462
Last_Name = 'Hwang'
First_Name = 'Jiwon'

def aes_enc(inputblock, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(inputblock)

def des_enc(inputblock, key):
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(inputblock)

def invertbit(data, bit):
    byte_index = bit // 8
    bit_index = bit % 8
    mask = 1 << (7 - bit_index)
    new_data = bytearray(data)
    new_data[byte_index] ^= mask
    return bytes(new_data)

def findbitdiff(a, b):
    return bin(int.from_bytes(a, 'big') ^ int.from_bytes(b, 'big')).count('1')

def des_input_av_test(inputblock, key, bitlist):
    # inputblock with size of 16 bytes and key with size of 8 bytes
    # bitlist is a list of integers that define the position of the
    # bit in the inputblock that needs to be inverted, one at a time, for example
    # [0, 3, 6, 25, 78, 127]
    
    # 1- any initializations necessary
    diff_list = []
    
    # 2- perform encryption of the original values
    #    anyway you like. It doesn't have to be with 
    #    this exact function form
    originalcipher = des_enc(inputblock, key)
    
    # 3- for every value given in the bitlist:
    for b in bitlist:
        #invert the value of the corresponding bit in the inputblock (doesn't have to be in this exact
        # function form)
        newinput = invertbit(inputblock, b)
        
        # perform encryption on the new input with one inverted bit at position b
        newcipher = des_enc(newinput, key)
        
        # find the number of bit differences between the two ciphertexts (doesn't have to be exactly in
        # this function form)
        # Use any method you like to find the difference. 
        numbitdifferences = findbitdiff(originalcipher, newcipher)
        
        # add it to the list
        diff_list.append(numbitdifferences)
        
    # return the list of numbers (this is the output used for grading your homework)
    return diff_list

# We also perform similar experiment by keeping the inputblock fixed and changing the
# selected bits of the key
def des_key_av_test(inputblock, key, bitlist):
    # inputblock with size 16 bytes and key with size 8 bytes
    # bitlist is a list of integers that define the position of the
    # bit in the key that needs to be inverted, one at a time, for example
    # [0, 3, 6, 25, 78, 127]
    
    # 1- any initializations necessary
    diff_list = []
    
    # 2- perform encryption of the original values
    #    anyway you like. It doesn't have to be with 
    #    with this exact function form
    originalcipher = des_enc(inputblock, key)
    
    # 3- for every value given in the bitlist:
    for b in bitlist:
        #invert the value of the corresponding bit in the key (doesn't have to be in this exact
        # function form)
        newkey = invertbit(key, b)
        
        # perform encryption with the new key with one inverted bit at position b
        newcipher = des_enc(inputblock, newkey)
        
        # find the number of bit differences between the two ciphertexts (doesn't have to be exactly in
        # this function form)
        numbitdifferences = findbitdiff(originalcipher, newcipher)
        
        # add it to the list
        diff_list.append(numbitdifferences)
        
    # return the list of numbers
    return diff_list
    
def aes_input_av_test(inputblock, key, bitlist):
    # inputblock with size of 16 bytes and key with size 16 bytes
    # bitlist is a list of integers that define the position of the
    # bit in the inputblock that needs to be inverted, one at a time, for example
    # [0, 3, 6, 25, 78, 127]
    
    # 1- any initializations necessary
    diff_list = []
    
    # 2- perform encryption of the original values
    #    anyway you like. It doesn't have to be with 
    #    this exact function form
    originalcipher = aes_enc(inputblock, key)
    
    # 3- for every value given in the bitlist:
    for b in bitlist:
        #invert the value of the corresponding bit in the inputblock (doesn't have to be in this exact
        # function form)
        newinput = invertbit(inputblock, b)
        
        # perform encryption on the new input with one inverted bit at position b
        newcipher = aes_enc(newinput, key)
        
        # find the number of bit differences between the two ciphertexts (doesn't have to be exactly in
        # this function form)
        # Use any method you like to find the difference. 
        numbitdifferences = findbitdiff(originalcipher, newcipher)
        
        # add it to the list
        diff_list.append(numbitdifferences)
        
    # return the list of numbers (this is the output used for grading your homework)
    return diff_list

# We also perform similar experiment by keeping the inputblock fixed and changing the
# selected bits of the key
def aes_key_av_test(inputblock, key, bitlist):
    # inputblock with size 16 bytes and key with size 16 bytes
    # bitlist is a list of integers that define the position of the
    # bit in the key that needs to be inverted, one at a time, for example
    # [0, 3, 6, 25, 78, 127]
    
    # 1- any initializations necessary
    diff_list = []
    
    # 2- perform encryption of the original values
    #    anyway you like. It doesn't have to be with 
    #    with this exact function form
    originalcipher = aes_enc(inputblock, key)
    
    # 3- for every value given in the bitlist:
    for b in bitlist:
        #invert the value of the corresponding bit in the key (doesn't have to be in this exact
        # function form)
        newkey = invertbit(key, b)
        
        # perform encryption with the new key with one inverted bit at position b
        newcipher = aes_enc(inputblock, newkey)
        
        # find the number of bit differences between the two ciphertexts (doesn't have to be exactly in
        # this function form)
        numbitdifferences = findbitdiff(originalcipher, newcipher)
        
        # add it to the list
        diff_list.append(numbitdifferences)
        
    # return the list of numbers
    return diff_list


if __name__ == "__main__":

    #Textbook examples validation: Both print output should be same in each case. This is just to verify the code works you can replace these with your own test cases.
    print("=========================TESTING_AES_INPUT_BOOK_EXAMPLE===============================")
    original = aes_enc(b'\x01\x23\x45\x67\x89\xab\xcd\xef\xfe\xdc\xba\x98\x76\x54\x32\x10',b'\x0f\x15\x71\xc9\x47\xd9\xe8\x59\x0c\xb7\xad\xd6\xaf\x7f\x67\x98')
    new = aes_enc(b'\x00\x23\x45\x67\x89\xab\xcd\xef\xfe\xdc\xba\x98\x76\x54\x32\x10',b'\x0f\x15\x71\xc9\x47\xd9\xe8\x59\x0c\xb7\xad\xd6\xaf\x7f\x67\x98')

    print(findbitdiff(original,new))
    print(aes_input_av_test(b'\x01\x23\x45\x67\x89\xab\xcd\xef\xfe\xdc\xba\x98\x76\x54\x32\x10',b'\x0f\x15\x71\xc9\x47\xd9\xe8\x59\x0c\xb7\xad\xd6\xaf\x7f\x67\x98',[7]))

    print("=========================TESTING_AES_KEY_BOOK_EXAMPLE===============================")

    original = aes_enc(b'\x01\x23\x45\x67\x89\xab\xcd\xef\xfe\xdc\xba\x98\x76\x54\x32\x10',b'\x0f\x15\x71\xc9\x47\xd9\xe8\x59\x0c\xb7\xad\xd6\xaf\x7f\x67\x98')
    new = aes_enc(b'\x01\x23\x45\x67\x89\xab\xcd\xef\xfe\xdc\xba\x98\x76\x54\x32\x10',b'\x0e\x15\x71\xc9\x47\xd9\xe8\x59\x0c\xb7\xad\xd6\xaf\x7f\x67\x98')

    print(findbitdiff(original,new))
    print(aes_key_av_test(b'\x01\x23\x45\x67\x89\xab\xcd\xef\xfe\xdc\xba\x98\x76\x54\x32\x10',b'\x0f\x15\x71\xc9\x47\xd9\xe8\x59\x0c\xb7\xad\xd6\xaf\x7f\x67\x98',[7]))

    print("=========================TESTING_DES_INPUT_BOOK_EXAMPLE===============================")
    original = des_enc(b'\x02\x46\x8a\xce\xec\xa8\x64\x20',b'\x0f\x15\x71\xc9\x47\xd9\xe8\x59')
    new = des_enc(b'\x12\x46\x8a\xce\xec\xa8\x64\x20',b'\x0f\x15\x71\xc9\x47\xd9\xe8\x59')

    print(findbitdiff(original,new))
    print(des_input_av_test(b'\x02\x46\x8a\xce\xec\xa8\x64\x20',b'\x0f\x15\x71\xc9\x47\xd9\xe8\x59',[3]))

    print("=========================TESTING_DES_KEY_BOOK_EXAMPLE===============================")

    original = des_enc(b'\x02\x46\x8a\xce\xec\xa8\x64\x20',b'\x0f\x15\x71\xc9\x47\xd9\xe8\x59')
    new = des_enc(b'\x02\x46\x8a\xce\xec\xa8\x64\x20',b'\x1f\x15\x71\xc9\x47\xd9\xe8\x59')

    print(findbitdiff(original,new))
    print(des_key_av_test(b'\x02\x46\x8a\xce\xec\xa8\x64\x20',b'\x0f\x15\x71\xc9\x47\xd9\xe8\x59',[3]))

    #From the homework description
    av_val=aes_input_av_test(b'thisoneis16bytes',b'veryverylongkey!',[5, 29, 38])
    print(av_val)
    assert av_val==[65, 67, 68], "Test Case 1: aes_input failed"

    av_val=aes_key_av_test(b'thisoneis16bytes',b'veryverylongkey!',[5, 29, 38])
    print(av_val)
    assert av_val==[61, 65, 65], "Test Case 2: aes_key failed"

    dv_val=des_input_av_test(b'thisoneis16bytes',b'deskey!!',[3, 25, 36])
    print(dv_val)
    assert dv_val==[27, 35, 28], "Test Case 3: des_input failed"
    
    
    dv_val=des_key_av_test(b'thisoneis16bytes',b'deskey!!',[3, 25, 36])
    print(dv_val)
    assert dv_val==[56, 68, 64], "Test Case 4: des_key failed"
    # Test cases for des_input_av_test
    print("=========================TESTING_DES_INPUT_AV_TEST===============================")
    des_input_test_cases = [
        (b'thisoneis16bytes', b'deskey!!', [3, 25, 36]),
        (b'1234567890abcdef', b'abcdefgh', [0, 7, 15]),
        (b'abcdefghijklmnop', b'12345678', [8, 16, 24]),
        (b'0987654321fedcba', b'87654321', [4, 12, 20]),
        (b'fedcba9876543210', b'abcdef12', [2, 10, 18]),
        (b'1122334455667788', b'99887766', [1, 9, 17]),
        (b'abcdefabcdefabcd', b'12341234', [5, 13, 21]),
        (b'1234123412341234', b'56785678', [6, 14, 22]),
        (b'8765432187654321', b'abcdefab', [11, 19, 27]),
        (b'abcdefabcdefabcd', b'12345678', [23, 31, 39])
    ]
    for inputblock, key, bitlist in des_input_test_cases:
        print(des_input_av_test(inputblock, key, bitlist))

    # Test cases for des_key_av_test
    print("=========================TESTING_DES_KEY_AV_TEST===============================")
    des_key_test_cases = [
        (b'thisoneis16bytes', b'deskey!!', [3, 25, 36]),
        (b'1234567890abcdef', b'abcdefgh', [0, 7, 15]),
        (b'abcdefghijklmnop', b'12345678', [8, 16, 24]),
        (b'0987654321fedcba', b'87654321', [4, 12, 20]),
        (b'fedcba9876543210', b'abcdef12', [2, 10, 18]),
        (b'1122334455667788', b'99887766', [1, 9, 17]),
        (b'abcdefabcdefabcd', b'12341234', [5, 13, 21]),
        (b'1234123412341234', b'56785678', [6, 14, 22]),
        (b'8765432187654321', b'abcdefab', [11, 19, 27]),
        (b'abcdefabcdefabcd', b'12345678', [23, 31, 39])
    ]
    for inputblock, key, bitlist in des_key_test_cases:
        print(des_key_av_test(inputblock, key, bitlist))

    # Test cases for aes_input_av_test
    print("=========================TESTING_AES_INPUT_AV_TEST===============================")
    aes_input_test_cases = [
        (b'thisoneis16bytes', b'veryverylongkey!', [5, 29, 38]),
        (b'1234567890abcdef', b'abcdefghijklmno!', [0, 7, 15]),
        (b'abcdefghijklmnop', b'1234567890abcdef', [8, 16, 24]),
        (b'0987654321fedcba', b'87654321abcdefgh', [4, 12, 20]),
        (b'fedcba9876543210', b'abcdef1234567890', [2, 10, 18]),
        (b'1122334455667788', b'9988776655443322', [1, 9, 17]),
        (b'abcdefabcdefabcd', b'1234123412341234', [5, 13, 21]),
        (b'1234123412341234', b'5678567856785678', [6, 14, 22]),
        (b'8765432187654321', b'abcdefabcdefabcd', [11, 19, 27]),
        (b'abcdefabcdefabcd', b'1234567890abcdef', [23, 31, 39])
    ]
    for inputblock, key, bitlist in aes_input_test_cases:
        print(aes_input_av_test(inputblock, key, bitlist))

    # Test cases for aes_key_av_test
    print("=========================TESTING_AES_KEY_AV_TEST===============================")
    aes_key_test_cases = [
        (b'thisoneis16bytes', b'veryverylongkey!', [5, 29, 38]),
        (b'1234567890abcdef', b'abcdefghijklmno!', [0, 7, 15]),
        (b'abcdefghijklmnop', b'1234567890abcdef', [8, 16, 24]),
        (b'0987654321fedcba', b'87654321abcdefgh', [4, 12, 20]),
        (b'fedcba9876543210', b'abcdef1234567890', [2, 10, 18]),
        (b'1122334455667788', b'9988776655443322', [1, 9, 17]),
        (b'abcdefabcdefabcd', b'1234123412341234', [5, 13, 21]),
        (b'1234123412341234', b'5678567856785678', [6, 14, 22]),
        (b'8765432187654321', b'abcdefabcdefabcd', [11, 19, 27]),
        (b'abcdefabcdefabcd', b'1234567890abcdef', [23, 31, 39])
    ]
    for inputblock, key, bitlist in aes_key_test_cases:
        print(aes_key_av_test(inputblock, key, bitlist))