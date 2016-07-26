#This program is designed to allow the user to input a message and apply
#a Ceasarian shift of the user's choice.



def encryptor(message,shift):
    Alphabet = (
    ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s',
    't','u','v','w','x','y','z']
    )

    #Decrypted is a list that will store each decrypted letter as part of a list.
    encrypted = []
    #Decrypted message will store the joined letters as one string
    encryptedmessage = ''
    length = len(message)


    #We use a for loop using in range rather than just by term because it makes the if statement work.
    #This for loop runs letter by letter through the input message to decrypt.
    for i in range(0,length):
        #letter is the current letter in the input message
        letter = message[i]
        #in order to account for spaces, we check to see if the current letter is a letter, char is each letter in alphabet
        if any(char == letter for char in Alphabet):
            #if the current letter is a letter, we use this for loop to identify which letter it is
            for j in range (0,25):
                if Alphabet[j] == letter:
                    #We get the position of the current letter then apply the shift
                    #to get the decrypted letter, appending ti to decrypted.
                    position = j
                    positionnew = position + shift
                    if positionnew > 25:
                        positionnew = positionnew - 26
                    encrypted.append(Alphabet[positionnew])
        else:
            #If the current letter is not a letter, we don't run an encryption and simply append the letter.
            encrypted.append(letter)
    #Because decrypted is an array, we must use join to turn it into a string, the
    #empty quotes are what display between each concatenated string.
    encryptedmessage = ''.join(encrypted)
    return encryptedmessage





def decryptor(message,shift):
    Alphabet = (
    ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s',
    't','u','v','w','x','y','z']
    )

    #Decrypted is a list that will store each decrypted letter as part of a list.
    decrypted = []
    #Decrypted message will store the joined letters as one string
    decryptedmessage = ''
    length = len(message)


    #We use a for loop using in range rather than just by term because it makes the if statement work.
    #This for loop runs letter by letter through the input message to decrypt.
    for i in range(0,length):
        #letter is the current letter in the input message
        letter = message[i]
        #in order to account for spaces, we check to see if the current letter is a letter, char is each letter in alphabet
        if any(char == letter for char in Alphabet):
            #if the current letter is a letter, we use this for loop to identify which letter it is
            for j in range (0,25):
                if Alphabet[j] == letter:
                    #We get the position of the current letter then apply the shift
                    #to get the decrypted letter, appending ti to decrypted.
                    position = j
                    positionnew = position - shift
                    if positionnew < 0:
                        positionnew = positionnew + 26
                    decrypted.append(Alphabet[positionnew])
        else:
            #If the current letter is not a letter, we don't run an encryption and simply append the letter.
            decrypted.append(letter)
    #Because decrypted is an array, we must use join to turn it into a string, the
    #empty quotes are what display between each concatenated string.
    decryptedmessage = ''.join(decrypted)
    return decryptedmessage
