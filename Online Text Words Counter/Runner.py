import Sorts
import Read_Websites as Rea

# listC = re.listC
# listC2 = re.listC2

# Organize the results
listC2, listC = Sorts.InsertionSort(Rea.listC2, Rea.listC)

print(' Words '.center(12 + 5, '#'))
for i in range (len(listC)):
    k,v = listC[i], listC2[i]
    print(k.ljust(12, ',') + str(v).rjust(5))
