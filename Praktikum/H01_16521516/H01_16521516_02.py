# NIM/Nama    : 16521516/Ahmad Nadil
# Tanggal     : 3 Oktober 2021
# Deskripsi   : Program Operasi Dua Bilangan

# Input Angka dan Operator
Angka1 = int(input('Masukkan angka pertama : '))
Angka2 = int(input('Masukkan angka kedua : '))
Operator = input('Masukkan operator [+ , - , * , / , %] : ')

# Algoritma Perhitungan
if Operator == '+' or Operator == '-' or Operator == '*' or Operator == '/' or Operator == '%': # Algoritma Jika Operator yang Dimasukkan Sesuai Ketentuan

    # Algoritma Operasi Pertambahan
    if Operator == '+': # Scan Operator yang Diinput
        Hasil = (Angka1) + (Angka2) # Mendefinisikan variabel 'Hasil' dengan Penjumlahan Angka 1 dan 2

    # Algoritma Operasi Pengurangan
    elif Operator == '-': # Scan Operator yang Diinput
        Hasil = (Angka1) - (Angka2) # Mendefinisikan variabel 'Hasil' dengan Pengurangan Angka 1 dan 2

    # Algoritma Operasi Perkalian
    elif Operator == '*': # Scan Operator yang Diinput
        Hasil = (Angka1) * (Angka2) # Mendefinisikan variabel 'Hasil' dengan Perkalian Angka 1 dan 2

    # Algoritma Operasi Pembagian
    elif Operator == '/': # Scan Operator yang Diinput
        Hasil = (Angka1) // (Angka2) # Mendefinisikan variabel 'Hasil' dengan Pembagian Angka 1 dan 2

    # Algortima Operasi Modulo
    elif Operator == '%': # Scan Operator yang Diinput
        Hasil = (Angka1) % (Angka2) # Mendefinisikan variabel 'Hasil' dengan Modulo Angka 1 dan 2

    # Output Hasil Akhir
    print(Angka1, Operator, Angka2, '=', Hasil)

# Algoritma Jika Operator yang Dimasukkan Salah
else:
    print('Operator yang anda masukkan salah!')
    print('Silakan ulangin program!')