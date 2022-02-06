# NIM/Nama : 16521516/Ahmad Nadil
# Tanggal : 27 Oktober 2021
# Deskripsi : Bilangan Tuan Dip dan Ric

# KAMUS
# N = Integer

# ALGORITMA
N = int(input('Masukkan bilangan Tuan Dip (N) : ')) # Input Bilangan Tuan Dip
M = N + 1
cek = True # Value Boolean dari 'cek'
while cek: # Looping ketika value 'cek' True

    # Cek digit dari bilangan Tuan Dip
    jumlah_N = 0 
    for x in str(N): 
        jumlah_N += int(x)

    #Cek digit dari bilangan Tuan Ric
    jumlah_M = 0
    for y in str(M):
        jumlah_M += int(y)
    
    # Meng-Break Looping jika kondisi terpenuhi, karena cek diupdate menjadi False
    if jumlah_N == jumlah_M:
        cek = False
        M -= 1
        
    M += 1

#Output AKhir 
print('Bilangan Tuan Ric adalah',M)
