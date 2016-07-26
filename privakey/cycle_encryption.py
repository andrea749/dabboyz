#This program is meant to allow user to input a message, specify cycle length
#and apply the cycle to decrypt a message.

import math

def cycle_encryptor(message, code_word):
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
    encrypted = []

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
            #This is the same as the caesarian_shift code.
            if any(char == letter for char in Alphabet):
                #if the current letter is a letter, we use this for loop to identify which letter it is
                for j in range (0,25):
                    if Alphabet[j] == letter:
                        #We get the position of the current letter then apply the shift
                        #to get the decrypted letter, appending it to decrypted.
                        position = j
                        positionnew = position + shifts[currentshift]
                        if positionnew > 25:
                            positionnew = positionnew - 26
                        encrypted.append(Alphabet[positionnew])
            else:
                #If the current letter is not a letter, we don't run an encryption and simply append the letter.
                encrypted.append(letter)

    #We do another for loop, however, instead of going through each cycle, we are
    #going through the remainder of the message after the last cycle.
    for ii in range (0, remain):
        letterpos = len(shifts) * cycle_number + ii
        letter = message[letterpos]
        if any(char == letter for char in Alphabet):
            #if the current letter is a letter, we use this for loop to identify which letter it is
            for j in range (0,25):
                if Alphabet[j] == letter:
                    #We get the position of the current letter then apply the shift
                    #to get the decrypted letter, appending ti to decrypted.
                    position = j
                    positionnew = position + shifts[ii]
                    if positionnew > 25:
                        positionnew = positionnew - 26
                    encrypted.append(Alphabet[positionnew])
        else:
            #If the current letter is not a letter, we don't run an encryption and simply append the letter.
            encrypted.append(letter)


    encryptedmessage = "".join(encrypted)

    return encryptedmessage



def cycle_decryptor(message, code_word):
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
            #This is the same as the caesarian_shift code.
            if any(char == letter for char in Alphabet):
                #if the current letter is a letter, we use this for loop to identify which letter it is
                for j in range (0,25):
                    if Alphabet[j] == letter:
                        #We get the position of the current letter then apply the shift
                        #to get the decrypted letter, appending it to decrypted.
                        position = j
                        positionnew = position - shifts[currentshift]
                        if positionnew < 0:
                            positionnew = positionnew + 26
                        decrypted.append(Alphabet[positionnew])
            else:
                #If the current letter is not a letter, we don't run an encryption and simply append the letter.
                decrypted.append(letter)

    #We do another for loop, however, instead of going through each cycle, we are
    #going through the remainder of the message after the last cycle.
    for ii in range (0, remain):
        letterpos = len(shifts) * cycle_number + ii
        letter = message[letterpos]
        if any(char == letter for char in Alphabet):
            #if the current letter is a letter, we use this for loop to identify which letter it is
            for j in range (0,25):
                if Alphabet[j] == letter:
                    #We get the position of the current letter then apply the shift
                    #to get the decrypted letter, appending ti to decrypted.
                    position = j
                    positionnew = position - shifts[ii]
                    if positionnew < 0:
                        positionnew = positionnew + 26
                    decrypted.append(Alphabet[positionnew])
        else:
            #If the current letter is not a letter, we don't run an encryption and simply append the letter.
            decrypted.append(letter)


    decryptedmessage = "".join(decrypted)

    return decryptedmessage
