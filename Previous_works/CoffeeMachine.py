# 3. This is a program of coffee machine (ask the user for coffees they like >> print the result >> ask if they are sure >> provide coffee)
import time

def menu(typeCoffee, size, sugar):
    "Prints the menu of the coffee machine"

    a=20+sugar
    b=30+sugar
    c=30+sugar
    d=50+sugar
    e=25+sugar
    f=40+sugar

    if typeCoffee==1 and size==2:
        print('1. Latte >> 2. Small >> price '+ str(a) +'NT' + ' >> 6sec') #a
    if typeCoffee==1 and size==1:
        print('1. Latte >> 1. Big >> price '+ str(b) +'NT'+ ' >> 6sec') #b
    if typeCoffee==2 and size==1:
        print('2. Americano >> 2. Small >> price '+ str(c) +'NT'+ ' >> 4sec') #c
    if typeCoffee==2 and size==2:
        print('2. Americano >> 1. Big >> price '+ str(d) +'NT'+ ' >> 4sec') #d
    if typeCoffee==3 and size==1:
        print('3. Expresso >> 2. Small >> price '+ str(e) +'NT'+ ' >> 5sec') #e
    if typeCoffee==3 and size==2:
        print('3. Expresso >> 1. Big >> price '+ str(f) +'NT'+ ' >> 5sec') #f
    print('Ready')
    return

cancel = False

while cancel==False:
    print('1. Latte  2. Americano  3. Expresso')
    typeCoffee = int(input('Please select the type of coffee you want: '))
    while typeCoffee!=1 and typeCoffee!=2 and typeCoffee!=3:
        typeCoffee = int(input('please enter the correct coffee: '))
    print('-------------------')
    print('1NT per Serve')
    sugar = int(input('Enter the amount of sugar you would like in range 0~5: '))
    while sugar!=1 and sugar!=2 and sugar!=3 and sugar!=4 and sugar!=5:
        sugar = int(input('please enter the correct amount of sugar: '))
    print('-------------------')
    print('1. BIG  2. SMALL')
    size = int(input('Please enter the size of coffee you would like: '))
    while size!=1 and size!=2:
        size = int(input('please enter the correct size: '))
    print('-------------------')

    menu(typeCoffee, size, sugar)
    #print(datetime.now())
    startTime = time.perf_counter()
    START=input('Please enter START in 10 seconds (or else the machine will start over): ')
    if time.perf_counter() - startTime <= 10:
        if START == "CANCEL":
            continue
        elif START == "START":
            cancel=True
            if typeCoffee==1:
                time.sleep(6)
                print("Here is your Latte~~~")
            if typeCoffee==2:
                time.sleep(4)
                print("Here is your Americano~~~")
            if typeCoffee==3:
                time.sleep(5)
                print("Here is your Expresso~~~")
            break
    else:
        continue
