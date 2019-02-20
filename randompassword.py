import random
import sys


try:
	passwordLength = int(sys.argv[1])
except:
	while True:
		try:
			passwordLength = int(input("How long do you want your password? (positive integer) :"))
			break
		except:
			pass

	
def randomPassword(length):
    shibboleth = ""
    while (len(shibboleth) < length):
        shibboleth += random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
    return shibboleth

print(randomPassword(passwordLength))

