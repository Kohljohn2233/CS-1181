# File Name: crypt_maker.py
# Date: 10/25/2021
# Class: CS 1181
# Name: Kohl Johnson
# Professor: Jon Holmes
# Description: Contains the functions needed to make a caesar and rolling type encryption

import random


def shift_letter(pre_shift_letter: str, shift_amount: int) -> str:
    """Shifts a letter by a certain amount, then returns that shifted letter"""
    perform_shift = True
    # Step 1: check if the letter is uppercase or not, if neither then don't shift ascii at all
    if ord("A") <= ord(pre_shift_letter) <= ord("Z"):
        is_capital = True
    elif ord("a") <= ord(pre_shift_letter) <= ord("z"):
        is_capital = False
    else:
        perform_shift = False

    # check if shift amount is positive or negative, set step amount accordingly
    if shift_amount < 0:
        step_amount = -1
    elif shift_amount > 0:
        step_amount = 1

    # Step 2: if perform_shift is True, then do exactly that
    if perform_shift:
        # set starting ascii value
        cur_ascii = ord(pre_shift_letter)

        # set min and max ascii value depending on if the letter is uppercase
        if is_capital:
            min_ascii = ord("A")
            max_ascii = ord("Z")
        else:
            min_ascii = ord("a")
            max_ascii = ord("z")

        # Step 3: Perform the shift
        for cur_shift in range(0, shift_amount, step_amount):
            # increase of decrease cur ascii by step_amount
            cur_ascii += step_amount

            # check to make sure cur_ascii is in bounds
            if cur_ascii < min_ascii:
                cur_ascii = max_ascii
            elif cur_ascii > max_ascii:
                cur_ascii = min_ascii

        # Step 4: Convert the ascii code to a character
        post_shift_letter = chr(cur_ascii)
    else:
        # if the letter is a special character then it cant be shifted, so we set that to the returning value
        post_shift_letter = pre_shift_letter

    # Step 5: Return the post_shift_letter
    return post_shift_letter


# -----------------------------------------------------------------------------------------------------------
# Caesar Encryption and Decryption

def caesar(pre_phrase: str, key: int) -> str:
    """Function to encrypt a phrase using a set shift amount"""
    encrypt_phrase = ""
    # Step 1: cycle through letters in the phrase and add them to the encrypt_phrase
    for each_letter in pre_phrase:
        # Step 2: run the shift_letter script to get the shifted letter
        encrypted_letter = shift_letter(each_letter, key)
        # Step 3: add the encrypted letter to the encrypted phrase
        encrypt_phrase += encrypted_letter

    # Step 4: return the encrypted phrase
    return encrypt_phrase


def caesar_back(enc_phrase: str, revert_key: int) -> str:
    """Takes a message encrypted by a set key and reverts it back to normal"""
    norm_phrase = ""
    revert_key = revert_key * -1
    # Step 1: cycle through each letter and add them to normal phrase
    for each_letter in enc_phrase:
        # Step 2: run the shift letter script to get the normal letter
        norm_letter = shift_letter(each_letter, revert_key)
        # Step 3: add the normal letter to the normal phrase
        norm_phrase += norm_letter

    # Step 5: return the normal phrase
    return norm_phrase


# -----------------------------------------------------------------------------------------------------------
# Rolling Type Encryption

def encrypt(pre_phrase: str, key: int) -> str:
    """Function to encrypt using a rolling type encryption"""
    roll_encryption = ""
    # Step 1: set the random seed to the key
    random.seed(key)
    # roll through each letter in the phrase and encrypt it
    for each_letter in pre_phrase:
        # Step 2: get a random number
        shift_number = random.randint(1, 25)
        # Step 3: encrypt the letter
        encrypt_letter = shift_letter(each_letter, shift_number)
        # Step 4: add the encrypt letter to the roll_encryption
        roll_encryption += encrypt_letter

    # Step 5: return the encrypted string
    return roll_encryption


def decrypt(encrypted_form: str, revert_key: int) -> str:
    """Takes the message encrypted by rolling encryption and reverts it back to normal"""
    norm_phrase = ""
    random.seed(revert_key)
    # Step 1: cycle through each letter
    for each_letter in encrypted_form:
        # Step 2: get the correct random number for decryption
        back_shift = random.randint(1, 25) * -1
        # Step 3: decrypt the letter
        norm_letter = shift_letter(each_letter, back_shift)
        # Step 4: add the norm letter to normal phrase
        norm_phrase += norm_letter

    # Step 5: return the normal phrase
    return norm_phrase


# -----------------------------------------------------------------------------------------------------------
# Stuff I used for testing the functions out
# phrase = "Kohlton Johnson"
# s_key = input("Enter the key: ")
# key = int(s_key)

# caesar_encryption = caesar(phrase, key)
# random_encryption = encrypt(phrase, key)

# caesar_decryption = caesar_back(caesar_encryption, key)
# random_decryption = decrypt(random_encryption, key)

# encryption_format = "Caesar Encryption: {0}\nRandom Encryption: {1}".format(caesar_encryption, random_encryption)
# decryption_format = "Caesar Decryption: {0}\nRandom Decryption: {1}".format(caesar_decryption, random_decryption)

# print(encryption_format)
# print(decryption_format)
