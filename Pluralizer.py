#This program get a int and string from the user, then checks if the string
#  enter by the user should be plural and return a correct string

A = {1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine',10:'Ten',}

# Get inputs from users
newWord = input("Enter a object: ")
quantity = int(input("Enter a number for quantity in range 1 to 10 (int): "))




def checkQuantity(quantity):
    """
    This function checks if the object has to be pluralize (quantity > 1)
    :param quantity: the amount of object enter by user
    :return: True or False
    """
    if quantity > 1:
        return True
    else:
        return False

def usual(quantity, newWord):
    """
    This function will check if the word needs to add 's' (common way)
    :param quantity: the amount of object enter by user
    :param newWord: the object enter by user
    :return: word + 's'
    """
    if checkQuantity(quantity) == True:
        if newWord.endswith("s") == False:
            newWord = newWord + "s"
    return newWord

def add_es(quantity, newWord):
    """
    This function will check if the word needs to add 'es'
    :param quantity: the amount of object enter by user
    :param newWord: the object enter by user
    :return: word + 'es'
    """
    if checkQuantity(quantity) == True:
        if newWord.endswith("sh") == True or newWord.endswith("ch") == True\
                or newWord.endswith("s") == True or newWord.endswith("x") == True or newWord.endswith("z") == True :
            newWord = newWord + "es"

    return newWord

def add_ves(quantity, newWord):
    """
    This function will check if the word needs to add 'ves'
    :param quantity: the amount of object enter by user
    :param newWord: the object enter by user
    :return: word + 'ves'
    """
    if checkQuantity(quantity) == True:
        if newWord.endswith("f") == True:
            newWord = newWord[:-1] + "ves"
        elif newWord.endswith("fe") == True:
            newWord = newWord[:-2] + "ves"

    return newWord

def add_s_ies(quantity, newWord):
    """
    This function will check if the word needs to add 'ies' or 's'
    :param quantity: the amount of object enter by user
    :param newWord: the object enter by user
    :return: word + 'ies' or 's'
    """
    if checkQuantity(quantity) == True:
        if newWord.endswith("y") == True:
            if newWord.endswith("ay") == True or newWord.endswith("ey") == True or\
                    newWord.endswith("iy") == True or newWord.endswith("oy") == True or newWord.endswith("uy") == True:
                newWord = newWord + "s"
            else:
                newWord = newWord[:-1] + "ies"

    return newWord

def add_s_es(quantity, newWord):
    """
    This function will check if the word needs to add 'es' or 's'
    :param quantity: the amount of object enter by user
    :param newWord: the object enter by user
    :return: word + 'es' or 's'
    """
    if checkQuantity(quantity) == True:
        if newWord.endswith("o") == True:
            if newWord.endswith("ao") == True or newWord.endswith("eo") == True or\
                    newWord.endswith("io") == True or newWord.endswith("oo") == True or newWord.endswith("uo") == True:
                newWord = newWord + "s"
            else:
                newWord = newWord + "es"

    return newWord


# check if the word fit in those rules
print(A[quantity], usual(quantity, add_ves(quantity, add_s_es(quantity, add_s_ies(quantity, add_es(quantity, newWord))))))






