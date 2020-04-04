import string
def validate_color(code):
    if code[0] != '#':
        print("Format kode Hex salah!")
        return
    
    code = code.split('#')
    colors = code[1]

    if len(colors) == 3 or len(colors) == 6:
        status = "Valid"
        for i in colors:
            if i in string.hexdigits:
                status = "Format kode Hex benar!"
            else:
                status = "Format kode Hex salah!"
                break
    else:
        status = "Format kode Hex salah!"
    
    print(status)
    return



validate_color('#123123')
validate_color('#abcde1')
validate_color('#0a0a1a')
validate_color('#0ga0aga')
validate_color('#02')

a = string.hexdigits