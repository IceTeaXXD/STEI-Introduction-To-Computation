# NIM/Nama  : 16521516/Ahmad Nadil
# Tanggal   : 11 Desember 2021
# Deskripsi : Kalkulasi Matrix


# Input Baris dan Kolom
b = int(input('Baris : ')) # Baris
k = int(input('Kolom : ')) # Kolom

# Mengisi Matrix sebanyak N Baris dan M Kolom dengan angka '0'
M = [[0 for j in range(k)] for i in range(b)] 
TotalM = 0

for i in range (b):
    for j in range (k):
        M[i][j] = int(input('Elemen[' + str(i) + '][' + str(j) + '] : ')) # Input Isi Matrix baris i kolom j
        TotalM += M[i][j]

x = int(input('Indeks baris dihapus = '))
y = int(input('Indeks kolom dihapus = '))

print (TotalM)
RataM = TotalM / (b*k)
print('Nilai rata-rata elemen matriks = ', RataM)

M1 = M

for i in range(b):
    for j in range(k):
        if j < x and i < y:
            M1[i][j] = M[i][j]
        elif j < x and i > y:
            M1[i-1][j] = M[i][j]
        elif j >= x and i < y:
            M1[i][j-1] = M[i][j]
        elif j >= x and i > y:
            M1[i-1][j-1] = M[i][j]

sum_M1 = 0
for i in range(b-1):
    for j in range(k-1):
        sum_M1 += M1[i][j]

RataM1 = sum_M1 / ((b-1)*(k-1))

print ('Nilai rata-rata elemen submatriks = ',RataM1)