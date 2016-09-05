#This program can check if the integer enter by user is within 10 of 100 to 200

import sys
print (sys.argv)
    
number = int(input("Please enter a integer between 100 to 200:"))
n=number%10

if 200<number or number<100:
    print('Please enter a correct integer between 100 to 200')
elif 100<=number<=200:
    if n==0:
        print('True')


sys.exit()
