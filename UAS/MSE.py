# NIM/Nama  : 16521516/Ahmad Nadil
# Tanggal   : 11 Desember 2021
# Deskripsi : Menghitung MSE

# KAMUS :
# n = integer
# T0,T1 = Array of integer

# ALGORITMA
# Input n sebagai banyak data
n = int(input('Masukkan Banyak Data : '))

# Cek untuk n harus bernilai > 0
if n <= 0: 
    print('Tidak ada data yang tersedia')

elif n > 0:
    T0 = [0 for i in range (n)]         # Isi array T0 dengan angka 0 sebanyak n
    for i in range (n):                 # Looping untuk isi Array T0
        T0[i] = int(input('Masukkan nilai ke-' + str(i+1) + ' data yang diamati : '))
    
    T1 = [0 for i in range (n)]         # Isi array T1 dengan angka 0 sebanyak n
    for i in range (n):                 # Looping untuk isi Array T1
        T1[i] = int(input('Masukkan nilai ke-' + str(i+1) + ' estimasi model komputasi : '))

    perhitungan = 0         # Set Value Awal Perhitungan = 0
    for i in range (0,n):   # Looping untuk menghitung fungsi yang berada di dalam sigma
        perhitungan += (int(T0[i]) - int(T1[i]))**2

    hasil = (1/n) * perhitungan     # Perhitungan akhir 

    # Output Akhir
    print('Hasil Akhir : ' ,hasil)