import random
def get_prop_formula():
        
    points = []
    numberOfCharacters = random.randint(1,4)
    characters = []

    for i in range(0,numberOfCharacters):
        NOT = random.randint(0,1)
        R = random.randint(65,90)
        if NOT == 0:
            characters.append(u'¬' + chr(R))
        else:
            characters.append(chr(R))

    symbols = []
    symbols.append(u'∧')
    symbols.append(u'→')
    symbols.append(u'∨')

    sentence = ''
    if len(characters) == 1:
        sentence = characters[0]
    else:
        for i in range(0,len(characters)):
            if i == len(characters) - 1:
                sentence += characters[i]
            else:
                sentence += characters[i] + symbols[random.randint(0,len(symbols)-1)]
    
    print(sentence)

get_prop_formula()
