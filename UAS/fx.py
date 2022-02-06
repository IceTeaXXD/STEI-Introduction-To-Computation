# NIM/Nama  : 16521516/Ahmad Nadil
# Tanggal   : 11 Desember 2021
# Deskripsi : Menghitung Hasil Dari Sebuah Fungsi

# KAMUS :
# n = masukan user (interger)
# x = masukan user (float)

# ALGORTIMA
# Membuat Fungsi perhitungan f(x) = 1 + x^1 + x^2 + .... + x^m
def deret(n,x):
    hasil = 0               # Set Value Awal Hasil = 0
    for i in range(0,n+1):  # Looping i sebagai pangkat dengan nilai 0 <= i < n+1
        hasil += x**i       # Looping penambahan value 'hasil' dengan x^i
    return hasil            # Return value akhir dari 'hasil' setelah looping selesai

# Input
n = int(input('Masukkan nilai n : '))       # Input nilai n banyak pengulangan perhitungan
x = float(input('Masukkan nilai x : '))     # Input nilai x sebagai angka yang dihitung

# Pemanggilan fungsi 'deret' dengan value n dan x
hitung = deret(n,x)

# Print Output Akhir
print('Hasil Akhir : ',hitung)