def isi(radit):
    for i in range(10):
        value = randint(0, 10)
        radit.append(value)
    return radit

def BacaArray(cek):
    x = 0
    for i in range(10):
        if T1[i] == T2[i]:
            x += 1
    if x == 10:
        cek = 'Array Sama'
    return cek

from random import randint
from random import seed
T1 = []
T2 = []
cek = 'Array Tidak Sama'
isi (T1)
isi (T2)
print (T1)
print(T2)
print(BacaArray(cek))