#create our own Caesarian Shift Cipher using ord (converts string to integer) and chr (converts integer to string)

# def caesar_cipher(plaintext,key):
#     ciphertext =''
#     for item in plaintext:
#         ciphertext_character_number_value = ord(item) + key
#         ciphercharacter = chr(ciphertext_character_number_value)
#         ciphertext = ciphertext + ciphercharacter
#     return ciphertext, -key
#
# encryptedmessage,userkey = caesar_cipher("hello", 13)
# print(encryptedmessage)
# decryptedmessage = caesar_cipher(encryptedmessage, userkey)
# print(decryptedmessage)

# listnumbers = [12,45,35,16,25,17,85,23,62,95,14,226,587,65,2,5586,20,14]
#
# for number in listnumbers:
#     if number%2==0:
#         print(f'{number} is even')
#     else:
#         print(f'{number} is odd')

# number = int(input("Please enter a number."))
# cal = number%3
# print(cal)

#let the sender matt determine prime number
#let the receiver tori determine primitive root
#let the private key serve as the exponent
#both sender and receiver create their own private key
#the firstroundcocreated key will be the second round primitve key
#all numbers must be integers

# fixed values for testing
# pubkey_matt = 9
# pvtkey_matt = 5
# pubkey_tori = 2
# pvtkey_tori = 4

pubkey_matt = int(input("Please enter a number for Matt's Public Key"))
pvtkey_matt = int(input("Please enter a number for Matt's Private Key"))
pubkey_tori = int(input("Please enter a number for Tori's Public Key"))
pvtkey_tori = int(input("Please enter a number for Tori's Private Key"))

matt_1st_cocreated = pubkey_tori**pvtkey_matt%pubkey_matt
tori_1st_cocreated = pubkey_tori**pvtkey_tori%pubkey_matt

# print(matt_1st_cocreated, tori_1st_cocreated)

matt_2_cocreated = tori_1st_cocreated**pvtkey_matt%pubkey_matt
tori_2_cocreated = matt_1st_cocreated**pvtkey_tori%pubkey_matt

print(matt_2_cocreated, tori_2_cocreated)