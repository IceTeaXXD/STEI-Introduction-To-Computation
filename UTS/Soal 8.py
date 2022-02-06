# NIM : 16521516
# Nama : Ahmad Nadil
# Deskripsi : Perkiraan penduduk

# KAMUS
# x = integer

#ALGORITMA
#INPUT
x = int(input("Masukkan nilai x: "))
Po = 1200000
k = 0.015
e = 1

# Looping untuk menghitung faktorial
for i in range(1, 101):
    penyebut = 1
    for j in range(1, i):
        penyebut *= i
    e += 1 / penyebut

# Looping print output pt
print("Perkiraan populasi penduduk kota A")
for i in range(x):
    Pt = Po * (e ** (k * (i+1))) / (10 ** 6)
    print('Tahun ke-' + str(i+1) + ' : ' + str(Pt) + ' juta')