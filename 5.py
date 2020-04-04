def findDuplicates(letter=None):
    if type(letter) != str:
        print("Harus memasukan parameter dan harus string!")
        return

    alphabet = {}
    for i in letter:
        if i not in alphabet:
            alphabet.update({i:1})
        elif i in alphabet:
            alphabet[i]+=1
    
    repeat = False
    for i,j in alphabet.items():
        if j > 1 and i != " ":
            print(i+":",j)
            repeat = True
            
    if repeat == False:
        print("Tidak ada karakter berulang")

findDuplicates()