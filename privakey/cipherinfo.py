#This file is basically just a dictionary of ciphers and their relevant
#information.




ciphers = {
    'cycle':{
        'name':'Vigenere',
        'description' : 'The Vigenere cipher is similar to the classic Caesarian shift but allows the user to create multiple values of offset. The image\
              below shows what each shift would look like.\
              <br>\
              <br>\
              <br>\
              <image id ="image" src = "../static/caesarshift2.jpg" width = "475" height = "200" alt = "Caesar cipher wheel">\
              <br>\
              <br>\
              <br>\
              The offsets are determined by a keyword chosen by the user. For example,\
              if the keyword is "abc" then the set of offsets would be 1,2,3 and every\
              third letter would be replaced by the next letter in the alphabet, every\
              letter after those would be replaced by the letter 2 places above in the\
              alphabet, and every letter after that would be replaced by the letter\
              3 places ahead. So, with a keyword "abc", "dadboyz" becomes "ecgcqba".\
              Note: If you alter the output text beyond simply copying it, you will\
              need to refresh the page to continue ciphering.'
    },
    'caesar':{
    'name': 'Caesar',
    'description':"The Caesar cipher is a classic cipher. The Caesar\
        cipher, also known as a rotation cipher, essentially involves shifting\
        the alphabet by a certain number. So in a Caesar cipher of 1, 'a'\
        becomes 'b', 'b becomes c, and so on with 'z' becoming 'a'. So in a Caesar\
        cipher of 1, 'dadboyz' becomes 'ebecpza'.\
        Note: If you alter the output text beyond simply copying it, you will\
        need to refresh the page to continue ciphering."
    },
    'trifid':{
    'name': 'Trifid',
    'description':"The Trifid cipher is based on a 3x3x3 cube. It works by assigning each letter of the alphabet three coordinates: layer, column, and row. It then takes these coordinates, prints them vertically, and then translates them horizontally. For example, the coordinates for 'dadboyz' would be:\
        <br>\
        <br>\
        <image id ='image' src = '../static/trifid.jpg' width = '212' height = '174' alt = 'Trifid coordinates'>\
        <br>\
        <br>\
        It then codes the words by reading the rows instead of columns. That way, the first two letters (111, 123) become 'ah' and 'dadboyz' becomes 'ahshebr'.\
        Note: If you alter the output text beyond simply copying it, you will\
        need to refresh the page to continue ciphering."
    },
    'columnar':{
    'name': 'Columnar Transposition',
    'description': 'Unlike the other ciphers on this cite, the Columnar Transposition\
    cipher is not a substitution cipher. Rather than encrypting each letter, this cipher\
    rearranges their order with the use of a key word. The letters of the message are\
    arranged into rows of the length of the key word. The columns are then rearranged\
    by the alphabetical order of the letters of the key word. For example, the message\
    "whereami" with the keyword "boys" would encrypt to "wehariem". The limits of this\
    cipher are that there can be no spaces and the length of the message must be a multiple\
    of that of the key word.\
    Note: If you alter the output text beyond simply copying it, you will\
    need to refresh the page to continue ciphering.'
    }
}
