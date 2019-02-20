import random
import sys


try:
	passwordLength = int(sys.argv[1])
except:
	passwordLength = input("How long do you want your password? ")

def randomPassword(length):
    shibboleth = ""
    while (len(shibboleth) < int(length)):
        shibboleth += random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
    return shibboleth

print(randomPassword(passwordLength))

