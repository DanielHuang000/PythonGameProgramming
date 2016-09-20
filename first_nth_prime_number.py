# This program prints out the first nth prime number, which n is enter by users
'''
n = int(input("Please enter a integer: "))
m = 0
while m in range (n):
    for x in range (2,100):
        y = x-1
        while y > 1:
            if not (x % y):
                continue
                y-=1
                print(x)
                m+=1


n = int(input("Please enter a integer: "))
notPrime = False
for m in range (2,n):
    if not (n % m == 0):
        notPrime = False
    else :
        print('No its not a prime number')
        notPrime = True
        break

if not notPrime:
    print('Yes ts a prime number')
'''


x = int(input("Please enter an integer for the first nth prime numbers: "))
n = 2
y = 0
while y <= x:
    notPrime = False
    for m in range (2, n):
        if not (n % m == 0):
            notPrime = False
        else :
            notPrime = True
            n+=1
            break

    if not notPrime:
        print(n)
        n+=1
        y+=1
