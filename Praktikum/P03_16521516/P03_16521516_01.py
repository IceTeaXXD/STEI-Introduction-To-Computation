# NIM/Nama : 16521516/Ahmad Nadil
# Tanggal : 3 November 2021
# Deskripsi : Menghitung Banyak Hari Tuan Dip Bisa Nonton

# KAMUS
# N = Integer
# k = Integer
# TabBiaya = Array [0..N-1] of integer

# ALGORITMA
N = int(input('Masukkan jumlah hari (N) : '))               # Input Jumlah hari 
k = int(input('Masukkan jumlah koin Tuan Dip (k) : '))      # Input Koin 
TabBiaya = [0 for i in range(N)]                            # Isi Array 'TabBiaya' dengan angka 0 sebanyak 'N'
Biaya = 0                                                   # Biaya Awal
Count = 0                                                   # Count adalah variabel untuk jumlah hari

for i in range (N):     # Looping untuk input angka ke dalam Array
    TabBiaya[i] = int(input('Biaya hari ke ' + str(i+1) + ' : '))

#Set biaya terkecil (minimum)
minimum = TabBiaya[0]

# Looping untuk membuat array urut dari nilai terkecil ke terbesar
for i in range(N):
    for j in range(i+1,N):
        if TabBiaya[i] > TabBiaya[j]:                           #Kondisi jika TabBiaya indeks [i] > indeks [j]
                                                                #*j adalah i+1
            TabBiaya[i],TabBiaya[j] = TabBiaya [j],TabBiaya[i]  #Jika kondisi terpenuhi, maka isi array akan ditukar dan diurutkan dari yang terkecil

# Looping untuk menentukan biaya yang harus dikeluarkan, mulai dari biaya terkecil
for j in range (N):
    Biaya += TabBiaya[j]
    if k >= Biaya : # Jika koin Tuan Dip masih lebih besar dari biaya total, maka 'Count' hari bertambah 1
        Count += 1

# Output Akhir
if Count > 0:       #Jika terdapat hari dimana Tuan Dip bisa bayar
    print('Maksimalnya adalah',Count,'hari')
elif Count == 0:    #Jika tidak terdapat hari dimana Tuan Dip bisa bayar
    print('Tuan Dip tidak bisa menonton TV ):')