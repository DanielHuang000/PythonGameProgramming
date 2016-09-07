#
import sys
number = int(input("Please enter a number: "))
a = 0
n = pow(10, a)
while number > n:
    a+=1
b = a
x = 1
if n > number:
    while b > 0:
        c = number % pow(10, (b-1))
        number /= pow(10, (b-1))
        print('Digit #{%d} = ' + str(c))%(x)
        b-=1
        x+=1


sys.exit(0)