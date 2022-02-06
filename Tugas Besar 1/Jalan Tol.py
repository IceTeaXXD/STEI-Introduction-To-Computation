#menentukan sisa uang pengguna jalan tol setelah membayar tarif tol
#mendefinisikan fungsi
def hasil(saldo,harga):
 sisauang = saldo - harga
 return sisauang

#Menginput matriks tarif tol berdasarkan tiga golongan 
tarifgol1=[[0, 300000, 275000, 150000, 50000], 
[300000,0,75000,200000,250000], [275000,75000,0,175000,225000], 
[150000,200000,175000,0,75000], [50000,250000,225000,75000,0]]
tarifgol2=[[0,325000,300000,175000,75000], [325000,0,100000,225000,275000],
[300000,100000,0,200000,250000], [175000,225000,200000,0,100000], 
[75000,275000,250000,100000,0]]
tarifgol3=[[0,350000,325000,200000,100000], 
[350000,0,125000,250000,300000], [325000,125000,0,225000,275000], 
[200000,250000,225000,0,125000], [100000,300000,275000,125000,0]]

#mengeluarkan kode kota sebagai referensi bagi pengendara
print("Nomor Kota Malang 0")
print("Nomor Kota Jakarta 1")
print("Nomor Kota Bandung 2")
print("Nomor Kota Jogja 3")
print("Nomor Kota Surabaya 4")
print(" ") #Menunjukkan spasi

#mengeluarkan spesifikasi golongan sebagai referensi
print("Golongan satu 0< panjang kendaraan <2.5 ,0< lebar kendaraan <1.5 dan 0< tinggi kendaraan <1")
print("Golongan dua 2.5<= panjang kendaraan <4 ,1.5<= lebar kendaraan <2.5 dan 1<= tinggi kendaraan <2")
print("Golongan tiga 4<= panjang kendaraan <8 ,2.5<= lebar kendaraan <3.5 dan 2<= tinggi kendaraan <5")
print(" ")

#menginput spesifikasi dan kota masuk serta kota keluar
p=float(input("Masukkan panjang kendaraan: "))
l=float(input("Masukkan lebar kendaraan: "))
t=float(input("Masukkan tinggi kendaraan: "))
x=int(input("Masukkan nomor kota masuk: "))
y=int(input("Masukkan nomor kota keluar: "))

#menentukan tarif dari input yang dimasukkan
jenis=[[ 0 for j in range(5)] for i in range(5)] #inisiasi jenis
harga=0
if(0<p<2.5 and 0<l<1.5 and 0<t<1):
    harga=harga+tarifgol1[x][y]
elif(2.5<=p<4 and 1.5<=l<2.5 and 1<=t<2):
    harga=harga+tarifgol2[x][y]
elif(4<=p<8 and 2.5<=l<3.5 and 2<=t<5):
    harga=harga+tarifgol3[x][y]
else:
    print("anda salah jalur")
print(" ") #menunjukkan spasi

#mengeluarkan tarif atau harga yang harus dibayar
if(harga==0):
    print("Maaf anda tidak dapat melanjutkan perjalanan silahkan rekam ulang kendaaraan")
else:
    print("Anda harus membayar: ",harga)
7
print(" ")

#menginput saldo agar tagihan bisa dibayar
if(harga==0):
    print("Silahkan keluar pintu tol sebelah kanan")
else:
    saldo=int(input("Silahkan masukkan saldo: "))
    if(saldo>harga):
        print("Sisa saldo anda: ",hasil(saldo,harga))
    else:
        print("Maaf saldo Anda kurang: ",str((-1)*hasil(saldo,harga)))
        print("Silahkan isi ulang saldo Anda")
        print("Silahkan keluar pintu tol sebelah kanan")
print(" ") #menunjukkan spasi

#mengeluarkan sisa uang dari hasil operasi saldo dan tarif/harga
print("Terima kasih dan selamat melanjutkan perjalanan")