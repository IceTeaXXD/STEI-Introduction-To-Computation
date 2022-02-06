def maks() : 
    maks = N[0]
    x = 0
    for i in range(100):
        if N[x] > maks:
            maks = N[x]
        x += 1
    return maks
def minim():
    minim = N[0]
    x = 0
    for i in range (100):
        if N[x] < minim:
            minim = N[x]
        x += 1
    return minim

from random import seed
from random import randint
N=[]
x=0
for i in range(100):
    value = randint(0, 11231)
    N.append(value)
print(N)

print('Nilai Minimum : ',minim())
print('Nilai Maksimal : ',maks())
