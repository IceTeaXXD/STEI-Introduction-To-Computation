x = int(input('Masukkan x : '))
y = int(input('Masukkan y : '))
z = int(input('Masukkan z : '))

i = 0
j = 0

f = 0

while i < x: 
    i += 1
    while j < y: 
        j += 1
        v = (i*x) + (j*y)
        if v == z:
            f += 1
            print(i,'kali ember x,',j,'kali ember y')

if f == 0:
    print('Tidak Mungkin')