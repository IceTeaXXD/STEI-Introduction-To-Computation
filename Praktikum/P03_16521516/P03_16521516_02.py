# NIM/Nama : 16521516/Ahmad Nadil
# Tanggal : 3 November 2021
# Deskripsi : Mengubah hurufnya terbanyak sebuah kata menjadi huruf R

# KAMUS
# N = Integer
# Kata = Integer
# Huruf = String

# ALGORITMA
N = int(input('Masukkan panjang kata Tuan Dip : '))     # Input Panjang Kata Tuan Dip
Kata = input('Masukkan kata Tuan Dip : ')               # Input Kata Tuan Dip
Huruf = ''          # Variabel untuk menempatkan huruf terbanyak dalam 'Kata'
count1 = 0          # Counter 1
count2 = 0          # Counter 2
New = ''            # String Kosong untuk Kata Baru setelah diganti R

# Looping untuk menentukan Huruf terbanyak dalam String
for i in range (N):
    for j in range (N):
        if Kata[i] == Kata[j]: # Kondisi Looping untuk cek apakah kata didalam string sama satu sama lain
            count1 += 1

    if count1 > count2:        # Kondisi untuk update huruf terbanyak dalam string
        count2 = 0             # Reset counter2
        Huruf = Kata[i]        # Assign String 'Huruf' dengan huruf terbanyak dalam string
        count2 = count1        # Value ounter 2 di set menjadi counter 1 agar kondisi ini jalan jika hanya ada huruf yang lebih banyak kesamaannya
    count1 = 0                 # Reset counter1

# Looping untuk mengganti huruf terbanyak menjadi R
for i in range (0,N):
    if Kata[i] == Huruf:        # Kondisi jika huruf dalam Kata Tuan Dip sama dengan huruf terbanyak
        New += 'R'              # Assign string New (String Kosong) dengan R

    else :                      # Kondisi jika huruf dalam Kata Tuan Dip tidak sama dengan huruf terbanyak
        New += Kata[i]          # Assign string New (string kosong) dengan huruf dalam Kata

# Output Akhir
print('Kata setelah diubah Tuan Ric adalah',New) 