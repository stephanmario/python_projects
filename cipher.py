#!/usr/bin/env/ python

#Decode ASCII encoded Caesar Cipher - Written for PYTHON 3
#To run in python 2.7, replace 'input' with 'raw_input'

print('Enter the cipher you want to decode, and guess the key.')

strASCII = ' 256 '
### This will hold all 256 ASCII chars

cyphertext = raw_input('Cyphertext: ')
#The encrypted string we want to decode

key = int(input('Key: '))
### Hint: less than 10 :-) ###

for i in range(256):
        strACSII = strASCII + chr(i)
### Create string with all 256 ASCII Chars ###

for x in range(len(cyphertext)):
        m = strASCII.find(cyphertext[x])
### m = position of this char within strASCII ###

print(cyphertext[x] + ' = ' + str(m) + ' = ' + chr(m-key))


#######################################################
#######################################################
## ALL DONE! better double check the code ROOKIE ;-) ##
#######################################################
#######################################################
