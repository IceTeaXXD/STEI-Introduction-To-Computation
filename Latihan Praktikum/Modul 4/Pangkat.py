def hitung(a,b,c,d):
    hasil = (a**b) + (c**d)
    return hasil
a = int(input('Masukkan bilangan a: '))
b = int(input('Masukkan bilangan b: '))
c = int(input('Masukkan bilangan c: '))
d = int(input('Masukkan bilangan d: '))
hasil = hitung(a,b,c,d)
print("")
print('Hasil perhitungannya adalah',hasil)