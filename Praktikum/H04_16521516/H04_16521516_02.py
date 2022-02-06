# NIM/Nama  : 16521516/Ahmad Nadil
# Tanggal   : 16 November 2021
# Deskripsi : Mengolah Isi Matrix

# KAMUS 
# N,M = Integer 
# TabA = Matrix [0..N-1][0..M-1] of integers

# ALGORITMA
# Pendefinisian Fungsi 'isiArray' Untuk Input isi Matrix
def isiMatrix(N,M,TabA,positif):
    # Looping untuk input isi matrix
    for i in range (N):
        for j in range (M):
            TabA[i][j] = int(input('Masukkan nilai A[' + str(i+1) + '][' + str(j+1) + '] : ')) # Input Isi Matrix baris i kolom j
            if TabA[i][j] > 0:      # Kondisi percabangan jika bilangan yang diinput > 0 (Positif)
                positif += 1        # Variabel counter 'positif' += 1 jika kondisi terpenuhi
    # Output banyaknya bilangan positif dalam matriks
    print('Ada',positif,'bilangan positif di matriks.')
    return TabA         # Return value dari TabA

# Pendefinisian Fungsi 'cetakMatrix' untuk Output Akhir dari Matrix
def cetakMatrix(N,M,baris):
    # Looping untuk output Matrix
    for i in range (N):
        for j in range(M):
            print (TabA[i][j],end=" ")     # Output Matrix baris i kolom j
            baris += 1                     # Variable counter 'baris' += 1
            if baris % M == 0:             # Kondisi percabangan jika banyak output sudah sebanyak N (Baris Matrix)
                print(" ")                 # Output untuk membuat baris baru

# Input Baris dan Kolom
N = int(input('Masukkan N : ')) # Baris
M = int(input('Masukkan M : ')) # Kolom

# Mengisi Matrix sebanyak N Baris dan M Kolom dengan angka '0'
TabA = [[0 for j in range(M)] for i in range(N)] 

positif = 0     # Pendefinisian variabel 'positif' sebagai counter
baris = 0       # Pendefinisian variable 'baris' sebagai counter

# Pemanggilan Fungsi 'isiMatrix'
isiMatrix(N,M,TabA,positif)

# Pemanggilan Fungsi 'cetakMatrix'
cetakMatrix(N,M,baris)