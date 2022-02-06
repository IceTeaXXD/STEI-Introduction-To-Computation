# NIM : 16521516
# Nama : Ahmad Nadil
# Deskripsi : Cek Tahun Kabisat 

# KAMUS
# N = Integer

#ALGORITMA
N = int(input('Masukkan Tahun : ')) #Input Tahun

if N > 0 : #Cek apakah N > 0
    if N % 100 == 0: #Cek apakah N tahun abad
        if N % 4 == 0 and N % 400 == 0: #Cek apakah N tahun abad dan merupakan tahun kabisat
            print(N,'merupakan tahun kabisat')

        else : #Jika N merupakan tahun abad dan bukan tahun kabisat
            print(N,'bukan merupakan tahun kabisat')

    elif N % 4 ==0: #Cek jika N merupakan tahun kabisat
        print(N,'merupakan tahun kabisat')

    else: #Hasil jika N bukan tahun kabisat
        print(N,'bukan tahun kabisat')

if N <= 0: #Hasil jika N 
    print('Tahun yang dimasukan salah')