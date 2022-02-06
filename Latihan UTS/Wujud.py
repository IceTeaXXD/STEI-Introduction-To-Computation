# NIM : 16521516
# Nama : Ahmad Nadil
# Deskripsi : Cek Wujud Air

# KAMUS
# suhu = Float

#ALGORITMA
suhu = float(input('Masukkan suhu air : '))
if suhu <= 0:
    print('wujud air beku')
elif 0 < suhu < 100:
    print('wujud air cair')
elif suhu >= 100 :
    print('wujud air uap')