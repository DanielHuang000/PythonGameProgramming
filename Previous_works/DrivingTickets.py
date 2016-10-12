#This program determin which tickets you will have to pay for your driving speed
#Enter yes if its your birthday, no if its not

import sys
print(sys.argv)
D=int(input("Please enter your driving speed"))
B=sys.argv[1]

if B=='yes':
    d=D-5
else:
    d=D

if d<=60:
    print('no ticket')
elif 60<d<=80:
    print('small ticket')
elif d>81:
    print('big ticket')



sys.exit(0)