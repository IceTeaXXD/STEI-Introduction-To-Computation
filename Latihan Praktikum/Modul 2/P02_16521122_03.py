# NIM/Nama  : 16521122/Kevin Prayoga Abdinegara
# Tanggal   : 27 Oktober 2021
# Deskripsi : Program input N dan mencari nilai maksimal dengan membagi N menjadi jumlah dari k bilangan positif syaratnya k >= 2, kemudian mengeluarkan output nilai maksimal dari perkalian bilangan tersebut.

# KAMUS
# N = integer

# ALGORITMA
# input
N = int(input('Masukkan bilangan N: '))

# N dalam beberapa kondisi
if N == 2 or N == 3: # jika N = 2 atau N = 3
    print('Nilai maksimalnya adalah {}.'.format(N - 1)) # output
else: # kondisi jika if salah
    result = 1 # batas bawah untuk loop dan print
    while(N > 4): # proses looping jika N > 4
        N -= 3
        result *= 3
    print(f'Nilai Maksimalnya adalah {N * result}.') # output akhir