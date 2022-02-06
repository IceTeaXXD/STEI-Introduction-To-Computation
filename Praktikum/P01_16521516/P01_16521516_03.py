# NIM/Nama  : 16521516/Ahmad Nadil
# Tanggal   : Rabu , 6 Oktober 2021
# Deskripsi : Program Perhitungan Biaya Parkir Beradasarkan Lama Parkir

# KAMUS
# lamaParkir = int

# ALGORITMA
lamaParkir = int(input('Masukkan waktu parkir: ')) # Input lama parkir dalam menit
biayaParkir = 0 # Pendefinisian biaya parkir awal, yaitu 0 rupiah
hargaParkir1 = 5000 # Harga Parkir 1 Jam Pertama
hargaParkir2 = 3000 # Harga Parkir 1 Jam berikutnya

# Jika lamaParkir <= 15 menit, biaya parkir = 0 dan penambahan tarif selanjutnya akan diabaikan
if lamaParkir <= 15: 
    biayaParkir = 0 
# Jika lamaParkir > 15 menit, biaya parkir akan terus ditambahkan dengan tarif parkir jika memenuhi syarat 
elif lamaParkir > 15: 
    if lamaParkir > 0: 
        biayaParkir += hargaParkir1 
    if lamaParkir > 60:
        biayaParkir += hargaParkir2
    if lamaParkir > 120:
        biayaParkir += hargaParkir2
    if lamaParkir > 180:
        biayaParkir += hargaParkir2
    if lamaParkir > 240:
        biayaParkir += hargaParkir2
    if lamaParkir > 300:
        biayaParkir = 20000

# Output Akhir Biaya Parkir
print('Tarif yang harus dibayar Tuan Ric sebesar',biayaParkir,'rupiah')






