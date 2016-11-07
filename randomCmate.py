

def randomCmate(inputList = ['Sabrina', 'Darren', 'Daniel', 'Stephanie', 'Cici']):

    """
    Selects a cleassmate at random
    :param inputList:
    :return:
    """
    import random as rn
    NumStu = len(inputList)
    P = rn.randint(NumStu)

    return inputList[P]


