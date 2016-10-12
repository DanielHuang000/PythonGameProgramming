import numpy as np
import matplotlib.pyplot as plt


legos = np.loadtxt('Legos.txt',delimiter=',')

#not sure how to use these...
"""
len(legos)
np.shape(legos)
for x, y in legos:
    print(x,y)
for x, y in legos:
    plt.show(x,y,color='gray')

plt.show()
"""

def distance(a,b):
    d=(a**2+b**2)**1/2
    return d

Bricks=0
Beams=0

for n in len(lego):
    x1=abs(x-3)
    y1=abs(x-5)
    x2=abs(x-7)
    y2=abs(x-4)
    distance(x,y)
    if (distance(x1,y1)<=distance(x2,y2)):
        Beams+=1
    else:
        Bricks+=1

print("Beams = " + str(Beams))
print("Bricks = " + str(Bricks))

