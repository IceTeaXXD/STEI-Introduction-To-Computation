# NIM/Nama    : 16521516/Ahmad Nadil
# Tanggal     : 3 Oktober 2021
# Deskripsi   : Program Pendefinisian Bilangan

# Input nilai x
x = int(input('Masukkan X : '))

# Algoritma Pendefinisian Bilangan

if x > 0: # Fungsi jika x > 0 (Bilangan Positif)

    if not x % 2 == 0: # Fungsi yang akan dijalankan jika x memiliki hasil bagi ketika dibagi 2 
                       # Angka yang memiliki hasil bagi ketika dibagi 2 adalah angka ganjil
        print('X adalah bilangan positif ganjil') # Print definisi X

    elif x % 2 == 0: # Fungsi yang dijalankan jika x tidak memiliki hasil bagi ketika dibagi 2
                    # Angka yang tidak memiliki hasil bagi ketika dibagi 2 adalah angka genap
        print('X adalah bilangan positif genap') # Print definisi X

elif x < 0: # Fungsi yang akan dijalankan jika x < 0 (Bilangan Negatif)
    print('X adalah bilangan negatif') # Print definisi X

elif x == 0 : # Fungsi yang akan dijalankan jika x = 0 (Bilangan Nol)
    print('X adalah bilangan nol')  # Print definisi X