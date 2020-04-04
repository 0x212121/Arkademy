from itertools import islice 
def divide(par1, par2):
    length = len(par1)
    result = []
    l = []
    for i in range(0, length, par2):
        l.append(par1[i])
    print(l)
    return True

divide([1,2,3,4,5], 2)
divide([1,2,3,4,5], 3)
divide([1,2,3,4,5], 1)