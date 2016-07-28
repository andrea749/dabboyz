#This program runs a columnar transposition cipher.

import math

def columnar_encryptor(message, code_word):
     Alphabet = (
     ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s',
     't','u','v','w','x','y','z']
     )

     cycle_size = len(code_word)

     length = len(message)

     cycle_number = int(math.floor(length / cycle_size))

     code_word = code_word.lower()


     code_word_list = []

     for letter in code_word:
         code_word_list.append(letter)

     code_word_list.sort()

     encrypted = []



     for i in range(0,len(code_word)):
         letter = code_word_list[i]
         j = code_word.index(letter)
         for sequence in range (0,cycle_number):
             position = j + len(code_word)*sequence
             encrypted.append(message[position])
     encryptedmessage = "".join(encrypted)
     return encryptedmessage






def columnar_decryptor(message, code_word):
     Alphabet = (
     ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s',
     't','u','v','w','x','y','z']
     )


     cycle_size = len(code_word)

     length = len(message)

     cycle_number = int(math.floor(length / cycle_size))

     code_word = code_word.lower()


     code_word_list = []

     for letter in code_word:
         code_word_list.append(letter)

     code_word_list.sort()

     decrypted = []



     for i in range(0,len(code_word)):
         letter = code_word[i]
         j = code_word_list.index(letter)
         for sequence in range (0,cycle_number):
             position = i + len(code_word) * sequence
             decrypted.append(message[position])
     decryptedmessage = "".join(decrypted)
     return decryptedmessage



# code_word = raw_input('Code word: ')
# message = raw_input('Message: ')
#
# print columnar_decryptor(message, code_word)





####
