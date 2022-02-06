# NIM/Nama  : 16521516/Ahmad Nadil
# Tanggal   : 16 November 2021
# Deskripsi : Segitiga Pascal

# KAMUS 
# N = Integer 
# Mat = Matrix [0..N-1][0..M-1] of integers

# ALGORITMA
N = int(input('Masukkan N : '))                     # Input N sebagai baris dan kolom matriks
Mat = [[1 for j in range(N)] for i in range (N)]    # Isi Matrix dengan angka 1 sebanyak N baris dan N kolom
baris = 0                                           # Pendefinisian counter 'baris' = 9

# Looping Untuk Menghitung Matrix Baris Baru
for i in range (1,N):
    for j in range (1,N):
        # Angka di baris selanjutnynya adalah penjumlahan angka diatas dan dikiri angka tersebut
        Mat[i][j] = Mat[i-1][j] + Mat[i][j-1]

# Looping Untuk Output Akhir
for i in range (N):
    for j in range(N):
        print(Mat[i][j],end= " ")      # Output Matrix baris i kolom j
        baris += 1                     # Variable counter 'baris' += 1
        if baris % N == 0:             # Kondisi percabangan jika banyak output sudah sebanyak N (Baris Matrix)
            print(" ")                 # Output untuk membuat baris baru