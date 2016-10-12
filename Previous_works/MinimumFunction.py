#This program finds the minimum of the function $4x^3 - 9x^2$

import math
from random import randint
x = randint(0,5)

a=int(input("Please enter a integer for a: "))
b=int(input("Please enter a integer for b: "))
c=int(input("Please enter a integer for c: "))
d=int(input("Please enter a integer for d: "))

def f(x, a, b, c, d):
    
    y = a*pow(x,b) - c*pow(x,d)
    return y


z = f(x, a, b, c, d)
n = f(x-1, a, b, c, d)
m = f(x+1, a, b, c, d)

print(z>n or z<m)
while z>n or z<m:
    x-=1
    z = f(x, a, b, c, d)
    n = f(x-1, a, b, c, d)
    m = f(x+1, a, b, c, d)

x+=1
print(x, f(x, a, b, c, d))
