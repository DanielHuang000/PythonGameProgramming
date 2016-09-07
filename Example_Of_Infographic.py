#This program translate a infographic picture in to a code that is able to interact with users.

a = input('Have you sneezed in the last hour? ')
if a == 'yes':
    e = input('Have you dusted your house recently? ')
    if e == 'yes':
        print('So you basically stir up the dust and make it angry?')
    elif e == 'no':
        print('Ok that is weird... ')
    else:
        f = input('then enter your reason of dusted your house: ')
        if f == 'I dont know':
            print('me too')
        else:
            print('Error! Please enter a correct reason')

elif a == 'no':
    b = input('Have you sneezed in the last week? ')
    if b == 'yes':
        print('Its ok, you are fine')
    elif b == 'no':
        c = input('Er...Are you undead or something? ')
        if c == 'yes':
            print('Umm...Ok I see...')
        elif c == 'no':
            d = input('So you are basically Superhuman?')
            if d == 'yes':
                print('You are crazy')
            elif d == 'no':
                print('You are answering question rendomly')
