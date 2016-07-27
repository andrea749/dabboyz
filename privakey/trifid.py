#This program is designed to turn an input message into its binary equivalent

from copy import copy

def find(needle,haystack):
  if needle == haystack: return []
  # Strings are iterable, too
  if isinstance(haystack,str) and len(haystack)<=1: return None
  try:
    for i,e in enumerate(haystack):
      r = find(needle,e)
      if r is not None:
        r.insert(0,i)
        return r
  except TypeError:
    pass
  return None

def slice_list(input, size):
    input_size = len(input)
    slice_size = input_size / size
    remain = input_size % size
    result = []
    iterator = iter(input)
    for i in range(size):
        result.append([])
        for j in range(slice_size):
            result[i].append(iterator.next())
        if remain:
            result[i].append(iterator.next())
            remain -= 1
    return result


def trifid_encryptor(message):
    Alphabet =([['a','b','c'],['d','e','f'],['g','h','i']],
    [['j','k','l'],['m','n','o'],['p','q','r']],
    [['s','t','u'],['v','w','x'],['y','z',' ']])

    AlphabetFlat = (
    ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s',
    't','u','v','w','x','y','z',' ']
    )

    encrypted = []
    encryptedmessage = ''

    #coordinatesEncrypted is the list of coordinates from message
    coordinatesEncrypted = []





    for j in range(0,len(message)):
        letter = message[j]
        letterlower = letter.lower()
        if (char == letterlower for char in Alphabet):
            encryptedletterCoord = find(letterlower, Alphabet)
            coordinatesEncrypted.append(encryptedletterCoord)

    #return coordinatesEncrypted
    #coordinatelist is the combined list of coordinates read horizontally
    coordinatelist = []

    #this nested for loop goes through the 3 rows and puts each coordinate into coordinatelist
    for coord in coordinatesEncrypted:
        try:
            coordinatelist = coordinatelist + [coord[0]]
        except:
            pass

    for coord in coordinatesEncrypted:
        try:
            coordinatelist = coordinatelist + [coord[2]]
        except:
            pass

    for coord in coordinatesEncrypted:
        try:
            coordinatelist = coordinatelist + [coord[1]]
        except:
            pass

    counter = 0
    for i in range(0,len(message)):
        letter = message[i]
        letterlower = letter.lower()
        i = i - counter
        if letterlower in AlphabetFlat:
            z_coord = coordinatelist[i * 3]
            row = coordinatelist[1 + i * 3]
            column = coordinatelist[2 + i * 3]
            if letter == letterlower:
                encrypted.append(Alphabet[z_coord][column][row])
            else:
                encrypted.append(Alphabet[z_coord][column][row].upper())
        else:
            encrypted.append(letter)
            counter += 1

    encryptedmessage = ''.join(encrypted)
    return encryptedmessage






def trifid_decryptor(message):
    Alphabet =([['a','b','c'],['d','e','f'],['g','h','i']],
    [['j','k','l'],['m','n','o'],['p','q','r']],
    [['s','t','u'],['v','w','x'],['y','z',' ']])

    AlphabetFlat = (
    ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s',
    't','u','v','w','x','y','z',' ']
    )

    decrypted = []
    decryptedmessage = ''

    #coordinatesDecrypted is the list of coordinates from message
    coordinatesDecrypted = []





    for j in range(0,len(message)):
        letter = message[j]
        letterlower = letter.lower()
        if (char == letterlower for char in Alphabet):
            try:
                decryptedletterCoord = find(letterlower, Alphabet)
                coordinatesDecrypted.append(decryptedletterCoord[0])
                coordinatesDecrypted.append(decryptedletterCoord[2])
                coordinatesDecrypted.append(decryptedletterCoord[1])
            except:
                pass

    #coordinatelist is the combined list of coordinates read horizontally
    coordinatelist = coordinatesDecrypted
    # for coord in coordinatesDecrypted:
    #     coordinatelist += coord
    # return  coordinatelist

    counter = 0

    splitCoordinateList = slice_list(coordinatelist,3)
    # return splitCoordinateList

    for i in range(0,len(message)):
        letter = message[i]
        letterlower = letter.lower()
        i = i - counter
        if letterlower in AlphabetFlat:
            z_coord = splitCoordinateList[0][i]
            row = splitCoordinateList[1][i]
            column = splitCoordinateList[2][i]
            if letter == letterlower:
                decrypted.append(Alphabet[z_coord][column][row])
            else:
                decrypted.append(Alphabet[z_coord][column][row].upper())

        else:
            decrypted.append(letter)
            counter += 1


    decryptedmessage = ''.join(decrypted)
    return decryptedmessage
