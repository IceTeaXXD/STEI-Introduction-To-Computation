# NIM/Nama  : 16521516/Ahmad Nadil
# Tanggal   : Rabu , 6 Oktober 2021
# Deskripsi : Program Penghitung Pajak Berdasarkan Penghasilan yang Diinput

# KAMUS
# Ujian1 = int
# Ujian2 = int
# Ujian3 = int
# Ujian4 = int


# ALGORITMA

# Input Nilai Ujian 1-4
Ujian1 = int(input('Masukkan nilai ujian 1: '))
Ujian2 = int(input('Masukkan nilai ujian 2: '))
Ujian3 = int(input('Masukkan nilai ujian 3: '))
Ujian4 = int(input('Masukkan nilai ujian 4: '))

# Menghitung Rata-Rata dari 4 Ujian
Rata = (Ujian1 + Ujian2 + Ujian3 + Ujian4) / 4

if Rata > 70 and Ujian1 > 50 and Ujian2 > 50 and Ujian3 > 50 and Ujian4 > 50 : # Command jika nilai ujian memenuhi syarat lulus
    print('Tuan Kil lulus kelas Tuan Ric.') # Output akhir

else : # Command jika nilai ujian tidak memenuhi syarat lulus
    print('Tuan Kil tidak lulus kelas Tuan Ric.') # Output akhir