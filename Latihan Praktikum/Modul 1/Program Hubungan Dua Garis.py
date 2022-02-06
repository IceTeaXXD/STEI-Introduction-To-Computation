# NIM/Nama  : 16521516/Ahmad Nadil
# Tanggal   : 3 Oktober 2021
# Deskripsi : Program Hubungan Dua Garis

# Intro
print('--------------------')
print('Program Menentukan Hubungan Antara Dua Garis')
print('--------------------')

print('Input persamaan garis yang diterima adalah')
print(' ')
print('Garis 1 => a1 X + b1 Y = c1')
print('Garis 2 => a2 X + b2 Y = c2')

# Input Nilai
print('--------------------')
print('INPUT PERSAMAAN GARIS')
print('--------------------')

print('Persamaan Garis 1')
a1 = int(input('Masukkan nilai a1 : '))
b1 = int(input('Masukkan nilai b1 : '))
c1 = int(input('Masukkan nilai c1 : '))

print('--------------------')

print('Persamaan Garis 2')
a2 = int(input('Masukkan nilai a2 : '))
b2 = int(input('Masukkan nilai b2 : '))
c2 = int(input('Masukkan nilai c2 : '))

print('--------------------')

# Algoritma Output Akhir
m1 = -a1 / b1
m2 = -a2 / b2

if m1 == m2:
    print('Kedua garis sejajar')
elif m1 == -1/m2:
    print('Kedua garis tegak lurus')
else : 
    print('Kedua garis tidak sejajar dan tidak tegak lurus')