# NIM : 16521516
# Nama : Ahmad Nadil
# Deskripsi : Perhitungan F(x)

# KAMUS
# a,b,x = float
# n = integer

#ALGORITMA
#INPUT
a = float(input('Nilai a : '))
b = float(input('Nilai b : '))
x = float(input('Nilai x : '))
n = int(input('Nilai N : '))
hasil = 0
for i in range (1,n+1):
    rumus = a*(x**i) + b
    hasil = hasil + rumus

print(hasil)