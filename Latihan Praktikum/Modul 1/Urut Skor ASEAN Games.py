# NIM/Nama  : 16521516/Ahmad Nadil
# Tanggal   : 3 Oktober 2021
# Deskripsi : Mengurutkan Nilai ASEAN Games

# INDONESIA
print('--------------------')
print('INPUT PEROLEHAN INDONESIA')
print('--------------------')
EmasI = int(input('Masukkan Emas Indonesia : '))
PerakI = int(input('Masukkan Perak Indonesia : '))
PerungguI = int(input('Masukkan Perunggu Indonesia : '))
SkorI = (5*EmasI + 3*PerakI + 1*PerungguI)

# SINGAPURA
print('--------------------')
print('INPUT PEROLEHAN SINGAPURA')
print('--------------------')
EmasS = int(input('Masukkan Emas Singapura : '))
PerakS = int(input('Masukkan Perak Singapura : '))
PerungguS = int(input('Masukkan Perunggu Singapura : '))
SkorS = (5*EmasS + 3*PerakS + 1*PerungguS)

print('--------------------')
print('HASIL')
print('--------------------')

# Algoritma Penentuan Urutan
if SkorI > SkorS :
    print('Pemenangnya adalah Indonesia')
elif SkorS < SkorI :
    print('Pemenangnya adalah Singapura')
elif EmasI > EmasS:
    print('Pemenangnya adalah Indonesia')
elif EmasI < EmasS:
    print('Pemenangnya adalah Singapura')
elif PerakI > PerakS:
     print('Pemenangnya adalah Indonesia')
elif PerakI < PerakS:
        print('Pemenangnya adalah Singapura')
elif PerungguI > PerungguS :
    print('Pemenangnya adalah Indonesia')
elif PerungguI < PerungguS:
    print('Pemenangnya adalah Singapura')      
else:
    print('Indonesia dan Singapura masih imbang')

""" # Algoritma Penentuan Urutan
if SkorI > SkorS :
    print('Pemenangnya adalah Indonesia')

elif SkorS < SkorI :
    print('Pemenangnya adalah Singapura')

elif SkorI == SkorS:
    if EmasI > EmasS:
        print('Pemenangnya adalah Indonesia')
    elif EmasI < EmasS:
        print('Pemenangnya adalah Singapura')

elif EmasI == EmasS:
    if PerakI > PerakS:
        print('Pemenangnya adalah Indonesia')
    elif PerakI < PerakS:
        print('Pemenangnya adalah Singapura')

elif PerakI == PerakS:
    if PerungguI > PerungguS :
        print('Pemenangnya adalah Indonesia')
    elif PerungguI < PerungguS:
        print('Pemenangnya adalah Singapura')

else:
    print('Indonesia dan Singapura masih imbang') """