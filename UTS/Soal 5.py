# NIM : 16521516
# Nama : Ahmad Nadil
# Deskripsi : Menghitung Nilai Rata-Rata Mahasiswa

# KAMUS
# NA, NB, NC, ND, NE = integer

#Algoritma

#INPUT
NA = int(input('Banyaknya SKS mata kuliah yang mendapat nilai A : '))
NB = int(input('Banyaknya SKS mata kuliah yang mendapat nilai B : '))
NC = int(input('Banyaknya SKS mata kuliah yang mendapat nilai C : '))
ND = int(input('Banyaknya SKS mata kuliah yang mendapat nilai D : '))
NE = int(input('Banyaknya SKS mata kuliah yang mendapat nilai E : '))

#RUMUS 
NR = ((NA*4) + (NB*3) + (NC*2) + (ND)) / (NA + NB + NC + ND + NE)

#OUTPUT 
print('Nilai Rata-Rata Mahasiswa :',NR)