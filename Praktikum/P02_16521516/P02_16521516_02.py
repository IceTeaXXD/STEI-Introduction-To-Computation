# NIM/Nama : 16521516/Ahmad Nadil
# Tanggal : 27 Oktober 2021
# Deskripsi : Banyaknya Triple a,b,c yang Dapat Dibentuk 

# KAMUS
# N = Integer

# ALGORITMA
N = int(input('Masukkan bilangan (N) : ')) # Input dari bilangan N
Hasil = 0 # Value awal dari banyak triplet

# Algoritma Looping yang memenuhi 1 <= a < b < c <= N
for a in range (1,N+1):
    for b in range (1,N+1):
        for c in range (1,N+1):     
            if a<b<c and a+b > c : # a+b > c adalah syarat dari sebuah segitiga adalah, jumlah dari dua sisi terkecil harus lebih besar dari sisi terpanjangnya
                                   # a<b<c adalah syarat dari soal 
                Hasil +=1 #Jika syarat dari segitiga terpenuhi, jumlah triplet yang mungkin akan ditambah dengan 1

#Output Akhir
print('Banyaknya triplet a,b,c adalah',Hasil)