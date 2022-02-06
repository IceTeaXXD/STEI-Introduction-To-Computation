import numpy as np
# Input Baris dan Kolom
b = int(input('Baris : ')) # Baris
k = int(input('Kolom : ')) # Kolom

# Mengisi Matrix sebanyak N Baris dan M Kolom dengan angka '0'
M = [[0 for j in range(k)] for i in range(b)] 

for i in range (b):
    for j in range (k):
        M[i][j] = int(input('Elemen[' + str(i) + '][' + str(j) + '] : ')) # Input Isi Matrix baris i kolom j

print (M)

x = int(input('Indeks baris dihapus = '))
y = int(input('Ineks kolom dihapus = '))

M1 = np.delete(M, x, y)
print (M1)