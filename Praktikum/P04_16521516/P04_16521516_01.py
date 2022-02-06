# NIM/Nama : 16521516/Ahmad Nadil
# Tanggal : 17 November 2021
# Deskripsi : Menghitung Rata-Rata Tertinggi Ujian

# KAMUS
# N,M = integer
# TabData = Matrix [0..N-1][0..M-1] of integers

# ALGORITMA
N = int(input('Masukkan banyak Mahasiswa (N): '))
M = int(input('Masukkan banyak Ujian (M): '))

# Variabel Counter
TotalNilai = 0
Mean = 0
Maks = 0
Tertinggi = ''
indeks = 0
N_Maks = 1

# Mengisi Matrix sebanyak N Baris dan M Kolom dengan angka '0'
TabData = [[0 for j in range(M)] for i in range(N)] 

# Looping Input Data
for i in range(N):
    for j in range (M):
        TabData[i][j] = int(input('Masukkan nilai Ujian ke ' + str(j+1) + ' mahasiswa ' + str(i+1) + ' : '))
    
    # Menghitung Jumlah Nilai Mahasiswa 'i'
    for j in range(M):
        TotalNilai += TabData[i][j]
    Mean = TotalNilai / M           # Rata-Rata Nilai Mahasiswa 'i'
    TotalNilai = 0                  # Reset Counter 'TotalNilai'
    
    # Percabangan untuk menentukan nilai tertinggi
    if Mean > Maks:
        Tertinggi = ''              # Reset String 'Tertinggi' dengan string kosoong
        Maks = Mean                 # Assign nilai maksimum dengan nilai Rata2 Mahasiswa 'i'
        Tertinggi += str(i+1)       # String 'Tertinggi' diisi dengan nomor mahasiswa 'i'

    # Percabangan jika terdapat nilai tertinggi antara mahasiswa yang sama
    elif Mean == Maks :
        if N_Maks == 1:             # Percabangan jika nilai maksimum baru berjumlah 1
            Tertinggi += ', '       # String 'Tertinggi' akan ditambah ', '
        Tertinggi += str(i+1)       # String 'Tertinggi' akan ditambah dengan nomor urut mahasiswa
        if i < N-1 :                # Percabangan untuk menulis koma
            Tertinggi += ', '
        elif i == N-1 :             # Percabangan untuk menulis titik
            Tertinggi += '.'
        N_Maks += 1

# Output Akhir
print('Mahasiswa dengan rata-rata tertinggi adalah mahasiswa ' + Tertinggi)