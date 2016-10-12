#This program ask the users several questions to determin if the user are able to use the picture he or she found.

a = input("Did you take or create the image yourself? ")
if a == 'yes':
    b = input('Was the picture you created an original idea?')
    if b == 'yes':
        print('Yes!')
    elif b == 'no':
        print('No!')
    else:
        print('When in doubt, do your research to find out if you copied an idea.'
              ' Otherwise, dont use the picture for anything other than limited personal use.')

elif a == 'no':

    c = input('Are you using the image for personal, non-profit, educational, research, or scholarly purposes'
               ' and are you using the image sparingly, only for limited purposes? ')
    if c == 'yes':
        print('Yes!')
    elif c == 'no':
        d = input('Are you transforming or repurposing the image to create a new purpose or meaning? ')
        if d == 'yes':
            print('Yes!')
        elif d == 'no':
            e = input('Are you publishing the image in a fact-based context or publication that benefits the public as a whole'
                       ' (such as in a news source where it is important that people see the image)? ')
            if e == 'yes':
                print('Probably')
            elif e == 'no':
                f = input('Would it be considered impossible to obtain permission from the original source? ')
                if f == 'yes':
                    print('Yes!')
                elif f == 'no':
                    print('Will you be using the inage for personal or commerical gain?'
                              '(If you answered "No" to all the fair use questions,'
                              ' the use of your image would most likely be considered for personal or commercial gain.)')
                    g = input('Is the image in the public domain or protected by creative commons agreements? ')
                    if g == 'yes':
                        print('Yes!')
                    elif g == 'no':
                        h = input('Did you purchase the image or obtain permission from the original source? ')
                        if h == 'yes':
                            print('Yes!')
                        elif h == 'no':
                            print('No!')

