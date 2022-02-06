kata = input("Masukkan string: ")
panjang = 0
#menentukan panjang kata
for char in kata: 
    panjang += 1
#jika tidak genap pasti salah
if panjang % 2 == 1: 
    print("Tidak Ganteng!")
else:
    reverse = ""
    #menentukan apakah string palindrom atau tidak
    for i in range(panjang-1, -1, -1): 
        reverse += kata[i]
    if reverse != kata:
        print("Tidak Ganteng!")
    else:
        #memisahkan string menjadi 2 string berbeda
        kiri = kata[:panjang//2]
        kanan = kata[panjang//2:]
        #membalik string kanan
        kananreverse = ""
        for i in range(panjang//2-1, -1, -1):
            kananreverse += kanan[i]
        #membalik string kiri
        kirireverse = ""
        for i in range(panjang//2-1, -1, -1):
            kirireverse += kiri[i]
        #mengecek apakah string kanan kiri palindrom
        if kiri == kirireverse and kanan == kananreverse:
            print("Ganteng!")
        else:
            print("Tidak Ganteng!")