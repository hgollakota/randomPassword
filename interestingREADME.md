randomPassWords.py
Uses argparse

Partially based on the idea expressed in this XKCD comic:
https://www.xkcd.com/936/

Utilizing words gathered from the New General Service List:
http://www.newgeneralservicelist.org/
Understanding the words in this wordset allows non-native
English speakers to comprehend an estimated 92% of the language

This program uses a wordbank stored as ngsl.txt
which should be saved in the same location as randomPassWords.py
for best effect.

To use:
In Command Prompt:
1) Navigate to the folder that contains both randomPassWords.py and ngsl.txt

ex:

c:\\> cd c:\\<folder>

2) Run randomPassWords.py from Commpand Prompt

OPTIONS:
There are several command prompt options that can be explained
by including -h or --help after the program

ex:

c:\\> randomPassWords.py -h

-Entering integers will specify a MINIMUM password length, default is 14

ex:

c:\\> randomPassWords.py 20

-the -wb or --wordbankfile option will allow use of a different wordbank
I have included a testwb.txt file to demonstrate this. Default is ngsl.txt,
but if that is unavailable a limited wordbank is included within the program
-the -n or --numbers option will include number 0-9 in the password
-the -s or --symbols option will include some special characters

ex:Basic Generation using defaults

c:\\Pyscripts>randomPassWords.py

Password :

ResistShapeAmendment

ex: Generating password with special characters

c:\\Pyscripts>randomPassWords.py 25 -s

Password :

Kid.Rather.Funny.Novel&Museum&

ex: Generating password with special characters and numbers

c:\\Pyscripts>randomPassWords.py 25 -sn

Password :

Although.3Regularly&6Blue.2

ex: Generating password using words from a different wordbank 

c:\\Pyscripts>randomPassWords.py 25 -sn -wb testwb.txt

Password :

Gzzle!5Lzzle!8Szzle.2Qzzle&7
