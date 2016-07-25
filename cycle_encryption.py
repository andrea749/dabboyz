#This program is meant to allow user to input a message, specify cycle length
#and apply the cycle to decrypt a message.

import math

Alphabet = (
['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s',
't','u','v','w','x','y','z']
)

message = raw_input('Enter your message: ')
#Asking how many different shifts user would like.
cycle_size = int(raw_input('What length of cycle would you like?'))
length = len(message)
shifts = []

#This for loop collects the different shifts from the user and stores in shifts.
for i in range (1, cycle_size + 1):
    shift = int(raw_input('Please enter the %d shift in the cycle: ' % (i)))
    shifts.append(shift)

#cycle_number is the number of full cycles required to run through the message.
#We floor it to make sure we don't exceed index.
cycle_number = int(math.floor(length / cycle_size))
print "cycle number: %d" % (cycle_number)
#remain is the remainder, we will cycle through this to go through whatever
#letters are left over as a result of rounding down cycle_number
remain = length % cycle_size
print remain
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
                    positionnew = position + shifts[currentshift]
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
                positionnew = position + shifts[currentshift]
                decrypted.append(Alphabet[positionnew])
    else:
        #If the current letter is not a letter, we don't run an encryption and simply append the letter.
        decrypted.append(letter)


decryptedmessage = "".join(decrypted)

print message
print decryptedmessage
