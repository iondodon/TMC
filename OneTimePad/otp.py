# implement one time pad


import random
import string


def generate_key(length) -> str:
    key = ''
    for i in range(length):
        key += random.choice(string.ascii_letters)
    return key


def encrypt(plaintext, key) -> str:
    ciphertext = ''
    for i in range(len(plaintext)):
        ciphertext += chr(ord(plaintext[i]) ^ ord(key[i % len(key)]))
    return ciphertext


def decrypt(ciphertext, key) -> str:
    plaintext = ''
    for i in range(len(ciphertext)):
        plaintext += chr(ord(ciphertext[i]) ^ ord(key[i % len(key)]))
    return plaintext


def main() -> None:
    key = generate_key(5)
    plaintext = 'This is a test'
    ciphertext = encrypt(plaintext, key)
    print('Plaintext: ', plaintext)
    print('Ciphertext: ', ciphertext)
    print('Decrypted: ', decrypt(ciphertext, key))


if __name__ == '__main__':
    main()