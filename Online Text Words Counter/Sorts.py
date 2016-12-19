import time
import Read_Websites as Rea

def sortHighToLow(listC2, listC):
    """
    This function use bubble sort to sort out the elements in the lists from high to low
    :param listC2: the list with all number
    :param listC: the list with all words
    :return: listC2 and listC
    """
    for i in range (len(listC2)):
        for j in range (len(listC2)-1-i):
            if listC2[j]<listC2[j+1]:
                listC2[j], listC2[j+1] = listC2[j+1], listC2[j]
                listC[j], listC[j+1] = listC[j+1], listC[j]
    return listC2, listC

# compete for speed
start = time.clock()
print(sortHighToLow(Rea.listC2, Rea.listC))
print(time.clock()-start)



def InsertionSort(items , listC):
    """
    This function use insertion sort to sort out the elements in the lists from high to low (faster method)
    :param items: the list with all number
    :param listC: the list with all words
    :return: items and listC
    """
    for i in range(1, len(items)):
        j=i
        while j>0 and items[j]>items[j-1]:
            items[j], items[j-1] = items[j-1], items[j]
            listC[j], listC[j-1] = listC[j-1], listC[j]
            j-=1
        else:
            continue
    return items, listC

# Compete for speed
start2 = time.clock()
print(InsertionSort(Rea.listC2, Rea.listC))
print(time.clock()-start2)
