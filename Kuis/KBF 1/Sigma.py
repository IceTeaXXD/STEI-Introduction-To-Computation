# NIM : 16521516
# Nama : Ahmad Nadil
# Deskripsi : Menghitung Jarak

#Kamus
# a,b = float
# n,x = integer

a = float(input('Masukkan nilai a : '))
b = float(input('Masukkan nilai b : '))
n = int(input('Masukkan nilai n : '))

indeks = 1
hitung = 0

for i in range (n):
    x = int(input('Masukkan nilai x ke-' + str(indeks) + ' : '))
    rumus = (a*x) + b
    hitung += rumus
    indeks += 1

print('Nilai Akhir :',hitung)