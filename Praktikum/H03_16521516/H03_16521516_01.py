# NIM/Nama  : 16521516/Ahmad Nadil
# Tanggal   : 2 November 2021
# Deskripsi : Membalikkan Array

# KAMUS 
# N = Integer 
# Angka = Array berisi integer 
# i = Integer

# ALGORITMA
N = int(input('Masukkan N : ')) #Input banyak bilangan yang ingin dimasukkan
Angka = [0 for i in range(N)] #Pendefinisian Angka sebagai Array berisi angka 0 sebanyak N

#Looping untuk input isi array, akan dilakukan input sebanyak N kali
for i in range (N): 
    Angka[i] = int(input()) #Update isi dari array untuk index i

print('Hasil Dibalik : ')

#Looping Mundur untuk print kebalikan isi array 
for i in range(N-1,-1,-1): #Looping dari N-1 menuju 0 dan terjadi pengurangan angka sebesar 1 terhadap nilai i setiap loopingnya
    print(Angka[i])