

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes
import time


UID = 121326492
First_Name = "Jiwon"
Last_Name = "Hwang"


# Function to get the current timestamp in milliseconds
def get_timestamp():
    return time.time()

# Function to generate RSA key pair
# n_bits is the RSA bit length Ex. 1024, 2048 ...
# must return private key and public key in PEM format
def generate_keypair(n_bits):
    key = RSA.generate(n_bits)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

# Function to encrypt a message using RSA public key
# Public key will be in PEM format
# must return encrypted message as bytes type
def rsa_encrypt_public(message, public_key):
    key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(key)
    encrypted_message = cipher.encrypt(message.encode())  # Encode the message to bytes
    return encrypted_message

# Function to decrypt a message using RSA private key
# private key will be in PEM format
# return decrypted message as string type
def rsa_decrypt_private(encrypted_message, private_key):
    key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(key)
    decrypted_message = cipher.decrypt(encrypted_message)
    return decrypted_message.decode()

def test_rsa_encryption_decryption():
    bit_list = [1024, 2048, 3072, 4096]
    test_cases = 20

    for bits in bit_list:
        for i in range(test_cases):
            # Generate RSA key pair
            private_key, public_key = generate_keypair(bits)

            # Message to encrypt
            message = "Test message " + str(i)
            print(f"Testing with message: {message}")

            # Encrypt the message
            encrypted_message = rsa_encrypt_public(message, public_key)

            # Decrypt the message
            decrypted_message = rsa_decrypt_private(encrypted_message, private_key)

            # Verify the decrypted message matches the original message
            assert decrypted_message == message, f"Decryption failed for message: {message}"

            print(f"Test case {i+1} for {bits}-bit key passed.")

    print("All test cases passed.")

# Call the test function
test_rsa_encryption_decryption()

# main
if __name__ == "__main__":

    bit_list = [1024, 2048, 3072, 4096]

    enc_len = []
    dec_len = []

    for bits in bit_list:

        # Generate RSA key pair
        private_key, public_key = generate_keypair(bits)

        #Print keys (optional)
        print("Private Key:")
        print(private_key.decode())
        print("\nPublic Key:")
        print(public_key.decode())

        # Message to encrypt
        message = "A" * 50

        # Encrypt the message and measure time
        start_time = get_timestamp()
        for _ in range(100):
            encrypted_message = rsa_encrypt_public(message, public_key)
        encryption_time = get_timestamp() - start_time
        enc_len.append(len(encrypted_message))



        print("\nEncrypted Message (in bytes):")
        print(encrypted_message)
        print(f"Encryption Time for {bits}-bit: {encryption_time:.6f} secs")


        # Decrypt the message and measure time
        start_time = get_timestamp()
        for _ in range(100):
            decrypted_message = rsa_decrypt_private(encrypted_message, private_key)
        decryption_time = get_timestamp() - start_time
        dec_len.append(len(decrypted_message))


        print("\nDecrypted Message:")
        print(decrypted_message)
        print(f"Decryption Time for {bits}-bit: {decryption_time:.6f} secs")


    assert enc_len==[128, 256, 384, 512], "Encryption length not matching"
    assert dec_len==[50,50,50,50], "Decryption length not matching"

    # DO NOT MODIFY MAIN UPTO THIS POINT

    
