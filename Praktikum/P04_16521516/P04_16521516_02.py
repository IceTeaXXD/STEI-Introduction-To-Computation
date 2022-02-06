# NIM/Nama : 16521516/Ahmad Nadil
# Tanggal : 17 November 2021
# Deskripsi : Penyingkatan Kata

# KAMUS
# N = integer

# ALGORITMA
# Input Banyak Kata
N = int(input("Masukkan banyak kata : "))

# Looping untuk input kata
for i in range(1,N+1):                  
    N_Kata = int(input('Masukkan panjang kata ke-' + str(i) + ' : '))
    Kata = input('Masukkan kata ke-' + str(i) + ' : ')

    #Pendefinisian Array kosong untuk Kata Baru
    KataBaru = []

    # Looping Mengisi Kata Baru
    for i in Kata:
        KataBaru.append(i)

    singkatan = ''

    # Looping membuat singkatan
    for i in KataBaru:
        if i in singkatan:
            continue
        singkatan += (i + str(KataBaru.count(i)))

    # Output Singkatan
    print('Singkatan katanya adalah',singkatan)