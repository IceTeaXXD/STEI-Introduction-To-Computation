# NIM/Nama  : 16521516/Ahmad Nadil
# Tanggal   : Rabu , 6 Oktober 2021
# Deskripsi : Program Penghitung Jumlah Mahasiswa yang Dibagi Ke Beberapa Kelas

# KAMUS
# Mahasiswa = int
# Kelas = int

# Algoritma
Mahasiswa = int(input('Masukkan jumlah mahasiswa: ')) #Input jumlah mahasiswa
Kelas = int(input('Masukkan jumlah kelas: '))         #Input jumlah kelas yang tersedia

Mahasiswa2 = Mahasiswa // Kelas # Pembagian mahasiswa setiap kelas
Kelas2 = Mahasiswa % Kelas      # Penentuan jumlah kelas

if Mahasiswa % Kelas == 0: # Command yang dijalankan jika mahasiswa bisa dibagi rata setiap kelasnya
    Jumlah = Mahasiswa // Kelas
    print('Setiap kelas memiliki', Jumlah ,'mahasiswa.')

else : # Command yang dijalankan jika mahasiswa TIDAK bisa dibagi rata setiap kelasnya
    print('Ada' , Kelas2 , 'kelas yang memiliki' , Mahasiswa2 + 1 , 'mahasiswa dan' , Kelas-Kelas2 , 'kelas yang mimiliki' , Mahasiswa2 , 'mahasiswa')
    # Mahasiswa2 + 1 untuk kelas pertama, karena pada pembagian terdapat pembulatan kebawah
    # Kelas - Kelas2 untuk menghitung jumlah kelas yang tersisa yang belum berisi mahasiswa