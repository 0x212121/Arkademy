import string
import re
def passwordCheck(password):
    if len(password) >= 9 and len(password) <= 15:
        print(bool(re.match(r'(?=.*[0-9])(?=.*[A-Z])(?=.*[a-z])(?=.*#)', password)))
    else:
        print(False)

def usernameCheck(username):
    if len(username) != 7:
        print("False")
        return False
    print(bool(re.match("[A-Z]{7}", username)))

usernameCheck("SABRINA")
usernameCheck("KEVIN")
passwordCheck("#DirumahAj4")
passwordCheck("Cuci#Tangan")