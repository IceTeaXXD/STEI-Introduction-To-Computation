# NIM/Nama : 16521516/Ahmad Nadil
# Tanggal : 17 November 2021
# Deskripsi : Mengisi Bensin

# KAMUS
# A, B, n = integer

# Pendefinsian Fungsi
def Hasil(s,a,b):
    ret = s
    for i in s:
        if i == a: 
            ret += str(b)
        else: 
            ret += str(a)
    return ret

# Input Variabel
A = input("Masukkan karakter 1: ")
B = input("Masukkan karakter 2: ")
n = int(input("Masukkan nilai n: "))

# Assign ans hasil sebagai A
ans = str(A)

# Looping Pemanggilan Fungsi
for i in range(1,n+1):
    ans = Hasil(ans,A,B)

# Output Akhir
print('Pola yang didapat :',ans)