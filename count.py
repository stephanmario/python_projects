#!/usr/bin/env python3
## this is a counting program ##

def testIfNumber(x):
    while True:    
        try:
            x = int(x)
            return int(x)
        except ValueError:
            x = input('Please enter a NUMBER: ')
	
Name = input('Please enter your name: ')

if(len(Name) <= 2):
    Name = input("Please enter a Name longer than TWO characters: ")
    
print('Good Day ' + Name)
    
print('Please enter the number that you want to start at.')
### The integer that we want to start at ###
CurrentNumber = testIfNumber(input('Start Point: '))


print('Now enter a number that you like to count by ')
### The number we are counting by ###
CountBy = testIfNumber(input('Count By: '))

print('And what number would you like to stop at?')
### The number we are going to count to ###
CountTo = testIfNumber(input('Stop At: '))

print('Now lets count :-]')

### the counting loop ###
for i in range(CurrentNumber,CountTo + CountBy,):
	print(i)
