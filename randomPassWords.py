# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 22:13:49 2019
File: 
Random word Password generator
by default requires ngsl.txt
@author: Harry
"""

import random
import argparse

#Ideally will never have to use this word bank, use in case ngsl.txt somehow is not available
useEmergency = False
emergencyBank = ['Alpha', 'Bravo', 'Charlie', 'Delta', 'Echo', 'Foxtrot', 'Golf', 'Hotel', 'India',
                    'Juliet', 'Kilo', 'Lima', 'Mike', 'November', 'Oscar', 'Papa', 'Quebec', 'Romeo', 
                    'Sierra', 'Tango', 'Uniform', 'Whisky', 'Xray', 'Yankee', 'Zulu', 'Alpha', 'Beta',
                    'Gamma', 'Delta', 'Epsilon', 'Zeta', 'Eta', 'Theta', 'Iota', 'Kappa', 'Lambda', 
                    'Mu', 'Nu', 'Xi', 'Omicron', 'Pi', 'Rho', 'Sigma', 'Tau', 'Upsilon', 
                    'Phi', 'Chi', 'Psi', 'Omega','Apple', 'Bat', 'Car', 'Dog', 'Egg', 'Fox', 
                    'Goat', 'Hi', 'Ink', 'Jack', 'Kiss', 'Lime', 'Mix','No', 'Orange', 'Pen', 'Quit', 
                    'Rose', 'Sing', 'Tiny', 'Ugly', 'Vine', 'Wine','X', 'Yes', 'Zen']

parser = argparse.ArgumentParser()
parser.add_argument("minsize", nargs='?', default=14,  help="Minimum Size of Password, default 14", 
                    type=int)
parser.add_argument("-wbf", "--wordbankfile", default="ngsl.txt", help="Different wordbank.txt file if desired")
parser.add_argument("-s", "-sp","-sym", "--symbols", action='store_true', 
                    help="Disallow special characters, default is allow")
parser.add_argument("-n", "--numbers", action='store_true', 
                    help="Include numbers 0-9 in password, default is no")
args = parser.parse_args()

try:
    file1 = open(args.wordbankfile,"r")
except:
    print("Invalid word bank .txt file. Trying default")
    try:
        file1 = open("ngsl.txt", "r")
    except:
        print("Using basic word bank")
        useEmergency = True


if not useEmergency:
    words = [l.lower().rstrip('\n') for l in file1.readlines()]
    words = [word.capitalize() for word in words]
    file1.close()
else:
    words = emergencyBank
    

shibboleth = ""
while (len(shibboleth) < args.minsize):
    shibboleth += random.choice(words)
    if args.symbols:
        shibboleth += random.choice("!&.")
    if args.numbers:
        shibboleth += random.choice("0123456789")

print("Password :")
print(shibboleth)
