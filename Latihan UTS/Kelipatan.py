# NIM : 16521516
# Nama : Ahmad Nadil
# Deskripsi : Print bilangan kelipatan 5 dalam suatu range dan menjumlahkannya

# KAMUS 
# N = integer 

# ALGORITMA
N = int(input('Masukkan N : '))
total = 0
for i in range(1,N+1):
    if i % 5 == 0:
        print(i,end=' ')
        total += i
print('')
print('total penjumlahan : ',total)