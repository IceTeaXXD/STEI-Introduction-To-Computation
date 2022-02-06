# NIM/Nama : 16521516/Ahmad Nadil
# Tanggal  : 3 Oktober 2021
# Deskripsi : Program Penentuan Indeks Akhir

print('--------------------')
print('Program Penentuan Indeks Akhir')
print('--------------------')

# Input Nilai
Nilai = float(input('Masukkan nilai akhir Tuan Mor : '))
print('--------------------')

# Algoritme Penentuan Indeks
if Nilai >= 80:
    Indeks = 'A'
elif 75 <= Nilai < 80:
    Indeks = 'AB'
elif 70 <= Nilai < 75:
    Indeks = 'B'
elif 60 <= Nilai < 70:
    Indeks = 'BC'
elif 50 <= Nilai < 60:
    Indeks = 'C'
elif 40 <= Nilai < 50:
    Indeks = 'D'
elif Nilai < 40:
    Indeks = 'E'

# Output Akhir
print('Tuan Mor mendapatkan indeks ' + Indeks)
print('--------------------')