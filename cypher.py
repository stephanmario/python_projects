#!/usr/bin/env python3
######################################################################
######    Decode ascii encoded CAESAR CIPHER - wirtten for python3 ###
###### to run in python 2.7 replace 'input' with 'raw_input' #########
######################################################################

strASCII = ''
for i in range(256): 
        strASCII = strASCII + chr(i)     

def encrypt(x):
    print('Enter the plaintext you wnat to encrypt.')     
    plaintext = input('plaintext: ')       
    for x in range(len(plaintext)):
        m = strASCII.find(plaintext[x])    
        print(plaintext[x] + ' = ' + str(m) + ' = ' + chr(m+key))
                
def decrypt(y):
    print('Enter the cypher you want to decode.') 
    cyphertext = input('Cyphertext: ')     ### The encrypted string we want to decode ###
    for y in range(len(cyphertext)):
        m = strASCII.find(cyphertext[y])    ### creates string with all 256 ASCII chars ####
        print(cyphertext[y] + ' = ' + str(m) + ' = ' + chr(m-key)) 

        



####################
### Name input #####
####################
#######       ######
########     #######
#########   ########
########## #########
print('Hello, please enter your name.')
input('Name: ')


########################
##### ADD VALIDATION ###
########################
encType = input('Would you like the encrypt or decrypt? ')
key = int(input('key: '))

if encType == 'encrypt':
    encrypt(encType)
    
elif encType == 'decrypt':
    decrypt(encType)
        
else: 
    while encType != 'encrypt' or encType != 'decrypt':
        print('PLEASE ENTER EITHER encrypt OR decrypt!!!')
        input('Try again: ')
