import time
#ALGORITMA
# Opening
print('---------------\nSELAMAT DATANG DI GERBANG TOL TRANSJAWA\n---------------')
time.sleep (0.5)
print('LIST GERBANG TOL')
time.sleep (0.2)
print(" ")

# List Gerbang Tol
gerbangTol = ['Merak','Cikupa','Jakarta Outer Ring Road','Cikampek','Palimanan','Kanci','Pejagan','Pemalang','Batang','Semarang (Kalikangkung)',
'Semarang ABC','Solo','Ngawi','Kertosono','Mojokerto','Surabaya','Gempol','Pasuruan','Probolinggo Timur']

nomorGerbang=1
for i in gerbangTol:
    print(nomorGerbang,':',i)
    nomorGerbang += 1
    time.sleep(0.07)

#List Harga Tol 
hargaTol = [44000,7500,15000,15000,107500,12000,29000,57500,39000,75000,5000,65000,91000,88000,49000,38000,4500,36000,26500]

""" ger=0
for i in gerbangTol:
    print(nomorGerbang,':',i,'( Rp.',hargaTol[ger],')')
    nomorGerbang += 1
    ger += 1
    time.sleep(0.07) """

# Input Gerbang Masuk
Masuk = int(input('Masukkan Nomor Gerbang Masuk : '))
Keluar = int(input('Masukkan Nomor Gerbang Keluar : '))
HargaAkhir = 0

# Ketersediaan Saldo
Saldo = int(input('Masukkan Saldo anda (Rp) : '))

# Output Tarif Tol
if Masuk < Keluar :
    for har in range(Masuk-1,Keluar-1):
        HargaAkhir += hargaTol[har]
    print('Tarif yang harus dibayar : Rp.',HargaAkhir)
elif Masuk > Keluar : 
    for har in range (Keluar-1,Masuk-1):
        HargaAkhir += hargaTol[har]
    print('Tarif yang harus dibayar : Rp.',HargaAkhir)

# Sisa Saldo
if Saldo > HargaAkhir:
    print('PEMBAYARAN BERHASIL')
    sisaSaldo = Saldo - HargaAkhir
    time.sleep(0.3)
    print('SISA SALDO ANDA : Rp.',sisaSaldo)
    time.sleep(0.3)
    print('GERBANG TERBUKA!!!!!! GASSKEEUNN NGENGENGENGEN')
else : 
    time.sleep(0.3)
    print('Anda Miskin!!!!! LMFAO')
    time.sleep(0.3)
    print('BALIK SONO')
