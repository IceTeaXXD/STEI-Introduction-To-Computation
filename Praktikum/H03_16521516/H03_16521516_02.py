# NIM/Nama  : 16521516/Ahmad Nadil
# Tanggal   : 2 November 2021
# Deskripsi : Anagram Dua Buah Array

# KAMUS 
# banyakA = Integer
# A = Array[0..banyakA-1] berisi Integer
# banyakB = Integer
# B = Array[0..banyakB-1] berisi Integer
# i,x,y = Integer

# ALGORITMA

# Pengisian Array A
banyakA = int(input('Masukkan banyaknya elemen A: ')) #Banyak elemen A
A = [0 for i in range (banyakA)]                      #Mengisi Array 'A' dengan angka 0 sebanyak 'banyakA'
for i in range (banyakA):                             #Looping isi Array
    A[i] = int(input('Masukkan elemen A ke-' + str(i+1) + ' : '))

# Pengisian Array B
banyakB = int(input('Masukkan banyaknya elemen B: ')) #Banyak elemen B
B = [0 for i in range (banyakB)]                      #Mengisi Array 'B' dengan angka 0 sebanyak 'banyakB'
for i in range (banyakB):                             #Looping isi Array
    B[i] = int(input('Masukkan elemen B ke-' + str(i+1) + ' : '))

# Pengecekan Anagram
cek = 0 #Variabel cek
for x in range(banyakA):     # Looping x dalam range banyakA untuk index array A
    for y in range(banyakB): # Looping y dalam range banyakB untuk index array B
        if A[x] == B[y]:     # Kondisi jika isi dari array A = isi dari array B, diperlukan untuk cek anagram
            cek += 1         # Variabel cek akan ditambah 1 jika kondisi terpenuhi

# Output Anagram
if cek == banyakA and banyakA == banyakB:  # Kondisi 1 : Jika banyak angka dalam kedua array sama dengan variabel cek anagram ('cek')
                                           # Kondisi 2 : Dapat dikatakan anagram jika jumlah angka dalam array A dan B sama
    print('B adalah anagram dari A')
else :                                     # Output Jika Kondisi tidak terpenuhi
    print('B bukan anagram dari A')