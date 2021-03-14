import random
#from sympy.abc import A, B, C
from sympy.logic.boolalg import to_dnf
from sympy.logic.boolalg import Or
from sympy.logic.boolalg import And
from sympy import Symbol 

def get_prop_formula():
    characters = ['A','B','C']
    operators = ['&','|']
    sentence = ''
    for i in range(0,4):
        if i == 3:
            sentence += characters[random.randint(0,2)]
        else:
            sentence += characters[random.randint(0,2)] + operators[random.randint(0,1)]
    print(sentence)
    return sentence

def convertToDNF():
    print(to_dnf(get_prop_formula()))
convertToDNF()