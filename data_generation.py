import random
from sympy.logic.boolalg import to_dnf, to_cnf
from sympy.logic.boolalg import Or
from sympy.logic.boolalg import And
from sympy.logic.boolalg import is_dnf , is_cnf
from sympy import simplify

from sympy import Symbol 

#function to make random propositional formulas
def get_prop_formula():
    characters = ['A','B','C','~A','~B','~C']
    operators = ['&','|']
    sentence = ''
    for i in range(0,4):
        if i == 3:
            sentence += characters[random.randint(0,2)]
        else:
            sentence += characters[random.randint(0,5)] + " " + operators[random.randint(0,1)]
    return sentence
#function to be used in calculator to convert propositional formula into DNF
def convertToDNF(formula):
    return to_dnf(formula)

#function to be used in calculator to convert propositional formula into CNF
def convertToCNF(formula):
    return to_cnf(formula)

#function to be used in practice part of the program to validate when user has to convert formula into CNF
def check_if_cnf(formula,userinput):
    x = convertToCNF(formula)
    x = str(x).replace(" ", "")
    userinput = str(userinput).replace(" ","")
    return(str(x) == str(userinput))
    

#function to be used in practice part of the program to validate when user has to convert formula into CNF
def check_if_dnf(formula,userinput):
    x = convertToDNF(formula)
    x = str(x).replace(" ", "")
    userinput = str(userinput).replace(" ","")
    return (str(x) == str(userinput))
    #return(str(x)==str(userinput))
    
# x = get_prop_formula()
# print(x)

# y = convertToDNF(x)
# print(y)

# print(check_if_dnf(y,y))