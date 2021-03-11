from itertools import product, tee

# Logic functions: take and return iterators of truth values
# Forked from https://gist.github.com/pindia/3836713
# Made by @GitHub user: pinda

def AND(a, b):
    for p, q in zip(a, b):
        yield p and q

def OR(a, b):
    for p, q in zip(a, b):
        yield p or q

def NOT(a):
    for p in a:
        yield not p

def EQUIV(a, b):
    for p, q in zip(a, b):
        yield p is q

def IMPLIES(a, b):
    for p, q in zip(a, b):
        yield (not p) or q

def create(num=2):
    ''' Returns a list of all of the possible combinations of truth for the given number of variables.
    ex. [(T, T), (T, F), (F, T), (F, F)] for two variables '''
    return list(product([True, False], repeat=num))

def unpack(data):
    ''' Regroups the list returned by create() by variable, making it suitable for use in the logic functions.
    ex. [(T, T, F, F), (T, F, T, F)] for two variables '''
    return [[elem[i] for elem in lst] for i, lst in enumerate(tee(data, len(data[0])))]

def print_result(data, result):
    ''' Prints the combinations returned by create() and the results returned by the logic functions in a nice format. '''
    n = len(data[0])
    dinesh = []
    headers = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:n]
    
    print(headers + "|RESULT")
    #dinesh.append(headers + "|RESULT")
    print('-' * len(headers) + '+------')
    
    for row, result_cell in zip(data, result):
        print(''.join({True: 'T', False:'F'}[cell] for cell in row) + '|' + '  ' + {True: 'T', False:'F'}[result_cell])
        dinesh.append([[{True: '1', False:'0'}[cell] for cell in row], {True: '1', False:'0'}[result_cell]])
    
    print("dinesh: ", dinesh)
    print("dinesh[0]: ", dinesh[0])
    print("dinesh[0][0]: ", dinesh[0][1])



if __name__ == '__main__':
    data = create(num=2)
    A, B = unpack(data)
    result = IMPLIES(A, B)
    print_result(data, result)