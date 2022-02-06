# NIM/Nama  : 16521516/Ahmad Nadil
# Tanggal   : 2 November 2021
# Deskripsi : Cek String Polindrom

# KAMUS 
# panjangText = Integer
# Text = string
# i = integer
# temp = string 

# ALGORITMA
panjangText = int(input('Masukkan panjang string : ')) # Input Panjang string
Text = input('Masukkan String : ')                     # Input Text (string)
                                                       # Asumsikan string hanya terisi huruf kecil semua

# Mengisi Variabel Temp Sebagai Kebalikan variabel Text
temp = "" # Pendefinisian Variabel Temp sebagai string kosong
for i in range (panjangText-1 , -1 , -1): # Looping mundur (terbalik) untuk mengisi variabel temp secara mundur
    temp += Text[i]                       # Mengisi variabel temp dari variabel Text secara terbalik

# Output
if Text == temp: # Kondisi jika text 'String' sama dengan text 'temp'
    print(Text, 'adalah palindrom')
else : 
    print(Text, 'bukan palindrom')