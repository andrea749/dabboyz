#This program runs a columnar transposition cipher.

import math

def columnar_encryptor(message, code_word):
     Alphabet = (
     ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s',
     't','u','v','w','x','y','z']
     )
     length = len(message)

     cycle_size = len(code_word)

     cycle_number = int(math.floor(length / cycle_size))

     code_word = code_word.lower()

     shifts = []

     code_word_list = []

     for letter in code_word:
         code_word_list.append(letter)

     code_word_list.sort()


     encryptedmessage = ''
     encrypted = []



     for i in range(0,len(code_word)):
         letter = code_word_list[i]
         j = code_word.index(letter)
         letterlower = letter.lower()
         #pregap is the number of characters in the message before the current column

     return encryptedmessage

# code_word = raw_input('Code word: ')
# message = raw_input('Message: ')
#
# print columnar_encryptor(message, code_word)






def columnar_decryptor(message, code_word):
     Alphabet = (
     ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s',
     't','u','v','w','x','y','z']
     )

     Alphashift = {
     'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,
     'm':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,
     'w':23,'x':24,'y':25,'z':26
     }


     length = len(message)


     cycle_size = len(code_word)

     code_word = code_word.lower()

     shifts = []

     for letter in code_word:
         shift = Alphashift[letter]
         shifts.append(shift)


     #cycle_number is the number of full cycles required to run through the message.
     #We floor it to make sure we don't exceed index.
     cycle_number = int(math.floor(length / cycle_size))
     print "cycle number: %d" % (cycle_number)
     #remain is the remainder, we will cycle through this to go through whatever
     #letters are left over as a result of rounding down cycle_number
     remain = length % cycle_size
     decrypted = []

     #So there are a number of nested for loops, the first we go through is one for
     #each COMPLETE cycle so we go through cycle_number.
     for currentcycle in range (0, cycle_number):
         #This second for loop goes through each individual cycle and identifies the
         #appropriate shift that needs to be made.
         for currentshift in range (0, len(shifts)):
             #The current letter of the message we are working on is found with
             #letterpos.
             letterpos = currentshift + currentcycle * len(shifts)
             letter = message[letterpos]
             letterlower = letter.lower()
             #This is the same as the caesarian_shift code.
             if any(char == letterlower for char in Alphabet):
                 #if the current letter is a letter, we use this for loop to identify which letter it is
                 for j in range (0,26):
                     if Alphabet[j] == letterlower:
                         #We get the position of the current letter then apply the shift
                         #to get the decrypted letter, appending it to decrypted.
                         position = j
                         positionnew = position - shifts[currentshift]
                         if positionnew < 0:
                             positionnew = positionnew + 26
                         if letterlower == letter:
                             decrypted.append(Alphabet[positionnew])
                         else:
                             decrypted.append(Alphabet[positionnew].upper())
             else:
                 #If the current letter is not a letter, we don't run an encryption and simply append the letter.
                 decrypted.append(letter)

     #We do another for loop, however, instead of going through each cycle, we are
     #going through the remainder of the message after the last cycle.
     for ii in range (0, remain):
         letterpos = len(shifts) * cycle_number + ii
         letter = message[letterpos]
         letterlower = letter.lower()
         if any(char == letterlower for char in Alphabet):
             #if the current letter is a letter, we use this for loop to identify which letter it is
             for j in range (0,26):
                 if Alphabet[j] == letterlower:
                     #We get the position of the current letter then apply the shift
                     #to get the decrypted letter, appending ti to decrypted.
                     position = j
                     positionnew = position - shifts[ii]
                     if positionnew < 0:
                         positionnew = positionnew + 26
                     if letter == letterlower:
                         decrypted.append(Alphabet[positionnew])
                     else:
                         decrypted.append(Alphabet[positionnew].upper())
         else:
             #If the current letter is not a letter, we don't run an encryption and simply append the letter.
             decrypted.append(letter)


     decryptedmessage = "".join(decrypted)

     return decryptedmessage
