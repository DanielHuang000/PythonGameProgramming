


def getInput(Grid, player):
    """
    This function get players' inputs and check for used space before enter the results
    :param Grid:
    :return:
    """
    A=True
    while A:
        Row = int(input(player + " please enter a number for row of next move: "))
        Column = int(input(player + " please enter a number for column of next move: "))
        if Grid[Row,Column] == ' ':
            Grid[Row,Column] = player
            A = False
        else:
            print("The space is fill already...Player1 please choose another coordinate")
    return Grid

def form(Grid):
    """
    This function prints out the form for the dictionary
    :param A:
    :return:
    """
    print(" ___ ___ ___")
    for x in range (1,4):
        for y in range (1,4):
            print("| "+ Grid[(x,y)] +" ", end='')
        print('|')
        for i in range (0,3):
            print("|___", end='')
        print('|')


def rules(Grid):
    """
    This function check for a winner
    :return: check
    """
    check = False #True if there is a winner
    for x in range (1,4):
        if Grid[(x,1)] == Grid[(x,2)] == Grid[(x,3)] and Grid[(x,1)]!=' ':
            check = True

    for y in range (1,4):
        if Grid[(1,y)] == Grid[(2,y)] == Grid[(3,y)] and Grid[(1,y)]!=' ':
            check = True

    if Grid[(1,1)] == Grid[(2,2)] == Grid[(3,3)] and Grid[(2,2)]!=' ':
        check = True
    elif Grid[(1,3)] == Grid[(2,2)] == Grid[(3,1)] and Grid[(2,2)]!=' ':
        check = True

    return check

def menu():
    """

    :return:
    """
    print()







