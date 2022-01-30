def process(message: str, key, type: str):
     # convert the message to uppercase
    message = message.upper()

    # convert the key to uppercase
    key = key.upper()

    # initialize the encrypted message
    new_message = ""

    # loop through the message
    for i in range(len(message)):

        # get the character
        character = message[i]

        # get the key character
        key_character = key[i % len(key)]

        # get the key value
        key_value = ord(key_character) - ord("A")

        # get the character value
        character_value = ord(character) - ord("A")

        if type == "encrypt":
            # add the key value to the character value
            character_value += key_value
        else :
            # subtract the key value from the character value
            character_value -= key_value

        # convert the character value back to a character
        character = chr(character_value % 26 + ord("A"))

        # add the character to the encrypted message
        new_message += character

    # return the new message
    return new_message


def encrypt(message, key):
    """
    Encrypt the message using the key
    """
    return process(message, key, "encrypt")


def decrypt(message, key):
    """
    Decrypt the message using the key
    """
    return process(message, key, "decrypt")


def main():

    # get the key
    key = input("Enter the key: ")

    # get the message
    message = input("Enter the message: ")

    # encrypt the message
    encrypted_message = encrypt(message, key)

    # print the encrypted message
    print("Encrypted message: ", encrypted_message)

    # decrypt the message
    decrypted_message = decrypt(encrypted_message, key)

    # print the decrypted message
    print("Decrypted message: ", decrypted_message)


if __name__ == "__main__":
    main()