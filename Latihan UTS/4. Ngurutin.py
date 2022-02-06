def inputan(): 
    a = int(input('Masukkan a : '))
    b = int(input('Masukkan b : '))
    c = int(input('Masukkan c : '))
    return a,b,c

""" def cek(a,b,c):
    if a > b > c:
        print(a,b,c)
    elif a > c > b:
        print(a,c,b)
    elif b > a > c:
        print(b,a,c)
    elif b > c > a:
        print(b,c,a)
    elif c > b > a:
        print(c,b,a)
    elif c > a > b:
        print(c,a,b)
    else : 
        print('Setiap bilangan harus berbeda') """

def cek(a,b,c):
    if a > b > c:
        hasil = a,b,c
    elif a > c > b:
        hasil = a,c,b
    elif b > a > c:
        hasil = b,a,c
    elif b > c > a:
        hasil = b,c,a
    elif c > b > a:
        hasil = c,b,a
    elif c > a > b:
        hasil = c,a,b
    else : 
        hasil = 'Setiap bilangan harus berbeda'
    return hasil

def outputan (hasil):
    print(hasil)

a,b,c = inputan()
hasil = cek(a,b,c)
outputan(hasil)