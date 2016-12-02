#!/usr/bin/env python3
#### Dice Roll Simulator ####
def roll(x):
    import random
    print(random.randint(1,6))

    
print('WELCOME TO A SMIPLE ROLL......... OF THE DICE ps: thank you for endulging my learning')
print('...... Buffering ........')

import time         ##### Creates a time delay for 6 seconds #####
time.sleep(6)       #####       ^^^^^^^^^^^^^^^^^            #####


print('Hello lets roll for you to show you how its done :-)' )
roll(1)

rollin = input('Would you like to roll again? Y/N: ')

if rollin == 'Y' or rollin == 'y':
    roll (rollin)
    while True:
        again = input('Would you like to roll again? Y/N: ')
        if again == 'Y' or again == 'y':
            roll(1)
        elif again == 'N' or again == 'n':
            print('Bye')
            exit()
            
elif rollin == 'N': 
    print('Goodbye')
    exit()
else:
    print('bye')