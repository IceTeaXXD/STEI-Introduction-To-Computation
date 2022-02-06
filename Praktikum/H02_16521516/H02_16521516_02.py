# NIM/Nama : 16521516/Ahmad Nadil
# Tanggal : 17 Oktober 2021
# Deskripsi : Menuliskan bilangan 10^x terkecil yang lebih dari N

# KAMUS 
# N = Integer 

# ALGORITMA
N = int(input('Masukkan N : ')) # Input Nilai N

x = 0 # Value Awal Pangkat

while (10 ** x) <= N: # Looping akan dijalankan jika 10^x <= N, yaitu sampai nilai 10^x melebihi nilai N, looping akan berhenti
    x += 1 # Value nilai x akan ditambah dengan 1 setiap looping

# Output Akhir
print('Hasil Akhir :', 10 ** x)