# I will be encrypting paswords using base64
import base64


introInput = input("if you want to encrypt your pasword enter e if you want to decrypt enter d: ")






def encryptPasswd(password):

    encodedBytes = base64.b64encode(password.encode())
    print(encodedBytes)

def decryptPasswd (password):
    decodeBytes = base64.b64decode(password)
    decodeData = decodeBytes.decode()
    print(decodeData)


if introInput == "e":
    usrPasswd = input("Please put your password down: ")
    encryptPasswd(usrPasswd)
elif introInput == "d":
    usrPasswd = input("Please put your encrypted password down: ")
    decryptPasswd(usrPasswd)
else:
    pass
