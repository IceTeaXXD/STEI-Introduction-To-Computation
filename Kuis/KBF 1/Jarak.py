# NIM : 16521516
# Nama : Ahmad Nadil
# Deskripsi : Menghitung Jarak

#Kamus
# S,T = float

#Algoritma
# Input
S = float(input('Masukkan Jarak Awal :'))
T = float(input('Masukkan Waktu Tempuh : '))
V = 10
a = (10 ** -2)

if S < 0 or T < 0:
    print('S dan T harus >= 0')

elif S >= 0 and T>= 0:
    #Rumus 
    St = (1/2 * a * (T**2)) + (V*T) + S

    #Output Akhir
    print('Jarak tempuh adalah',St)