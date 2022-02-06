# NIM/Nama : 16521516/Ahmad Nadil
# Tanggal : 27 Oktober 2021
# Deskripsi : Print dengan pola sifat menurun

# KAMUS
# x,n = integer

# ALGORITMA
x = int(input('Masukkan kelipatan : '))
N = int(input('Banyak suku yang diinginkan : '))

# Kelipatan yang pertama
x_pertama = x
# Variabel counter
p = 0

for i in range(1, N+1):
    # Output Kelipatan yang Dihasilkan
    print(x-p, end=' ')
    p += 1

    # Cek apakah output kelipatan sudah mencapai P suku dan update bilangan X dengan menambahkan dengan dirinya sendiri
    if p == x_pertama:
        x += x_pertama
        p = 0