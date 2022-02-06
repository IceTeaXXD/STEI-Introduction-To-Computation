# NIM/Nama : 16521516/Ahmad Nadil
# Tanggal : 10 Desember 2021
# Deskripsi : Penghitung Jarak

# KAMUS
# s0 = integer
# t = integer

# ALGORITMA
a = 10 ** -2
v = 10

s0 = int(input('Masukkan Jarak Awal : '))
t = int(input('Masukkan waktu tempuh : '))

st = (1/2 * a * (t)**2) + v*t + s0

print('Jarak akhir adalah : ', st)