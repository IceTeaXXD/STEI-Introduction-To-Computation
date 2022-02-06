# Kamus 
# a = integer
# b = integer
# n = integer

# Input a, b, dan n
a = int(input('Masukkan nilai a : '))
b = int(input('Masukkan nilai b : '))
n = int(input('Penjumlahan semua suku ke-n : '))

# Value awal dari sum
sum = 0

# ALGORITMA
if n > 0: 
    for i in range (n): # Looping
        # Rumus S(n) = a + (n-1)b
        sum += a + (i * b) # Penambahan sum secara looping dengan suku ke-n
    # Output Akhir 
    print('Hasil Dari Penjumlahan' , n , 'Suku adalah' , sum) 

else : # Dijalankan ketika n tidak sesuai
    print('Silakan Memasukkan n > 0')