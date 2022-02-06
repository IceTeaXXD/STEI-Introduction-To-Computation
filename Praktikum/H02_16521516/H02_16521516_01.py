# NIM/Nama : 16521516/Ahmad Nadil
# Tanggal : 17 Oktober 2021
# Deskripsi : Menuliskan Angka 1 Sampai N dalam Satu Baris

# KAMUS 
# N = Integer 

#ALGORITMA
N = int(input('Masukkan N : ')) #Input N

x = 1 # Variabel X Sebagai batas bawah untuk loop dan print, yaitu 1

for i in range(N): # Looping ketika variabel i berada dalam range dibawah N / Looping sampai N kali
    print(x, end=" ") # Print nilai variabel x dalam 1 baris
                      # Fungsi end=" " berguna supaya x di print dalam  baris
    x += 1 # Nilai x ditambahkan satu kali setiap looping