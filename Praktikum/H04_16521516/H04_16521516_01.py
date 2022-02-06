# NIM/Nama  : 16521516/Ahmad Nadil
# Tanggal   : 16 November 2021
# Deskripsi : Menghitung Fungsi Persamaan

# KAMUS 
# A,B = Integer

# ALGORITMA
# Pendefinisian Fungsi F(x)
def persamaan(x):
    hasil = (x**2) - (2*x) + 5  # Fungsi untuk menghitung f(x) = x^2 -2x + 5
    return hasil                # return value 'hasil'

# Input Variabel A & B
A = int(input('Masukkan A : '))
B = int(input('Masukkan B : '))

# Looping untuk print dan menghitung persamaan berdasarkan A dan B
for i in range (A,B+1):
    hasil = persamaan(i)                                # Memanggil Fungsi 'persamaan'
    print('f(' + str(i) + ')' + ' = ' + str(hasil))     # Output Akhir