'''
TUGAS BESAR PERHITUNGAN TARIF JALAN TOL

16521494 - Justin Yusuf Abidjoko
16521496 - Kelvin Rayhan Alkarim
16521516 - Ahmad Nadil
16521534 - Raditya Naufal Abiyu
'''

import time

gerbangTol = ['Merak','Cikupa','Jakarta Outer Ring Road','Cikampek','Palimanan','Kanci','Pejagan','Pemalang','Batang','Semarang (Kalikangkung)',
'Semarang ABC','Solo','Ngawi','Kertosono','Mojokerto','Surabaya','Gempol','Pasuruan','Probolinggo Timur']
hargaTol = [44000,7500,15000,15000,107500,12000,29000,57500,39000,75000,5000,65000,91000,88000,49000,38000,4500,36000,26500]

def opening():
    print('-----------------------------------\nSELAMAT DATANG DI GERBANG TOL TRANSJAWA\n-----------------------------------')
    time.sleep (0.5)
    print('LIST GERBANG TOL')
    time.sleep (0.2)
    print(" ")
    nomorGerbang=1
    for i in gerbangTol:
        print(nomorGerbang,':',i)
        nomorGerbang += 1
        time.sleep(0.07)
    print('-----------------------------------')

def harga_total(Masuk,Keluar):
    HargaAkhir=0
    if Masuk < Keluar :
        for har in range(Masuk-1,Keluar-1):
            HargaAkhir += hargaTol[har]
        print('Perjalanan dari "', gerbangTol[Masuk-1],'" ke "',gerbangTol[Keluar-1],'"')

    elif Masuk > Keluar : 
        for har in range (Keluar-1,Masuk-1):
            HargaAkhir += hargaTol[har]
        print('Perjalanan dari "', gerbangTol[Keluar-1],'" ke "',gerbangTol[Masuk-1],'"')

    print('Tarif Total : Rp.',HargaAkhir)
    return HargaAkhir

def gerbang(total_harga,saldo):
    if saldo >= total_harga:
        print('-----------------------------------')
        print('PEMBAYARAN BERHASIL')

        saldo = saldo - total_harga
        time.sleep(0.3)
        print('SISA SALDO ANDA : Rp.',saldo)
        print('-----------------------------------')

        temp = 0
        titik = '.' 
        while temp < 35:
            time.sleep(0.05)
            print(titik)
            titik += '.'
            temp += 1
        
        print('-----------------------------------\nGERBANG TERBUKA\nSILAHKAN JALAN\n-----------------------------------')

    else : 
        time.sleep(0.3)
        print('-----------------------------------\nSALDO TIDAK MENCUKUPI\nSEGERA HUBUNGI PETUGAS\n-----------------------------------')

opening()

Masuk = int(input('Masukkan Nomor Gerbang Masuk : '))
Keluar = int(input('Masukkan Nomor Gerbang Keluar : '))

if 1 <= Masuk <= 19 and 1 <= Keluar <= 19: 
    print('---------------')
    Total=harga_total(Masuk,Keluar)
    print('---------------')
    Saldo = int(input('Masukkan Saldo anda (Rp) : '))
    gerbang(Total,Saldo)

else : 
    print('Gerbang Tol Tidak Tidak Diketahui\nSilakan Hubungi Petugas')