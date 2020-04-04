def divide(mylist, chunk_size):
    result = []
    for i in range(0, len(mylist), chunk_size):
        result.append(mylist[i:i+chunk_size])

    if len(result[-1]) == 1 and chunk_size != 1:
        result[-2].append(*result[-1])
        del result[-1]
    return print(result)


divide([1,2,3,4,5], 2)
divide([1,2,3,4,5], 3)
divide([1,2,3,4,5], 1)