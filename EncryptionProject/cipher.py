# File Name: cipher.py
# Date: 10/25/2021
# Class: CS 1181
# Name: Kohl Johnson
# Professor: Jon Holmes
# Description: The "front page" of the program. Gathers input data and runs functions from crypt_maker.py

# get starting info
import crypt_maker

message = input("Enter message to encrypt: ")
s_key = input("Enter integer key: ")
key = int(s_key)

# get data
caesar_encryption = crypt_maker.caesar(message, key)
caesar_decryption = crypt_maker.caesar_back(caesar_encryption, key)

rolling_encryption = crypt_maker.encrypt(message, key)
rolling_decryption = crypt_maker.decrypt(rolling_encryption, key)

# headers
header_one = "---------- Caesar -----------"
header_two = "---------- Rolling ----------"

side_header_one = "Encrypted:"
side_header_two = "Decrypted:"

# data strings
caesar_header = "{0}".format(header_one)
caesar_row_one = "{0} {1}".format(side_header_one, caesar_encryption)
caesar_row_two = "{0} {1}".format(side_header_two, caesar_decryption)

rolling_header = "{0}".format(header_two)
rolling_row_one = "{0} {1}".format(side_header_one, rolling_encryption)
rolling_row_two = "{0} {1}".format(side_header_two, rolling_decryption)

# printing
print("\n" + caesar_header + "\n" + caesar_row_one + "\n" + caesar_row_two)
print("\n" + rolling_header + "\n" + rolling_row_one + "\n" + rolling_row_two)
