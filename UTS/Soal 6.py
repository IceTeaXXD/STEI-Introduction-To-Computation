# NIM : 16521516
# Nama : Ahmad Nadil
# Deskripsi : Penentuan Golongan Darah Anak

# KAMUS
# Ix, Iy = String

# ALGORITMA
#INPUT
Ix = input('Masukkan Ix Anak (IA/IO/IB) : ')
Iy = input('Masukkan Iy Anak (IA/IO/IB) : ')

#PERCABANGAN
if Ix == 'IA':
    if Iy == 'IA':
        print ('Golongan Darah Anak : A')
    elif Iy == 'IB':
        print ('Golongan Darah Anak : AB')
    elif Iy == 'IO':
        print ('Golongan Darah Anak : A')

elif Ix == 'IB' and (Iy == 'IB' or Iy == 'IO'):
    print ('Golongan Darah Anak : B')

elif Ix == 'IO' and Iy == 'IO':
    print ('Golongan Darah Anak : B')