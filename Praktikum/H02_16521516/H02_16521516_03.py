# NIM/Nama : 16521516/Ahmad Nadil
# Tanggal : 17 Oktober 2021
# Deskripsi : Cek Bilangan Prima 

# KAMUS
# x = integer

# ALGORITMA
x = int(input('Masukkan X : '))

# define variable 'definisi' sebagai boolean False
definisi = False

# x > 1, karena bilangan prima bernilai > 1
if x > 1:
    # Cek faktor yang bisa membagi x
    for i in range(2, x):
        if (x % i) == 0:
            # Looping ini berguna untuk mengecek apakah ada bilangan yang bisa membagi habis bilangan tersebut,
            # jika ada, maka bilangan bukan prima
            definisi = True #Update value 'definisi' menjadi True
            
elif x <= 1:
    definisi = True # Jika x <= 1, maka x bukan prima
                    # Update value 'definisi' menjadi True

# Cek jika definisi merupakan boolean True
if definisi: # Kondisi yang dijalankan jika value 'definisi' True
    print(x, 'bukan bilangan prima')
else: # Kondisi yang dijalankan jika value 'definisi' False
    print(x, 'adalah bilangan prima')