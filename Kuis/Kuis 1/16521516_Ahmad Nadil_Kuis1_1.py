# KAMUS
# lebarDada = integer

print('PROGRAM PENENTU UKURAN BAJU')

# Input Lebar Dada
lebarDada = int(input('Masukkan Lebar Dada (cm) : '))

# ALGORITMA

if 0 < lebarDada <= 54: # Ukuran yang Tersedia
    if 0 < lebarDada <= 46: # Ukuran S = 46 cm
        ukuranBaju  = 'S' 
    elif 46 < lebarDada <= 48: # Ukuran M = 48 cm
        ukuranBaju = 'M'
    elif 48 < lebarDada <= 50: # Ukuran L = 50 cm
        ukuranBaju = 'L'
    elif 50 < lebarDada <= 52: # Ukuran XL = 52 cm
        ukuranBaju = 'XL'
    elif 52 < lebarDada <= 54: # Ukuran XXL = 54 cm
        ukuranBaju = 'XXL'
    # Output Ukuran Baju
    print('Ukuran Baju yang Cocok adalah' , ukuranBaju)


if lebarDada > 54:  # Ukuran tidak tersedia jika lebar dada > 54 cm
    print('Tidak ada ukuran kaos yang cukup.')

if lebarDada < 0 : # Jika lebar dada salah
    print('Lebar Dada harus bilangan positif')
