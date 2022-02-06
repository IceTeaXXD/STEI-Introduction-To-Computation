N = int(input('Masukkan N : '))
volume =[]
x = 1
for i in range(N):
    p = int(input('Masukkan panjang balok ' + str(x) + ' : '))
    l = int(input('Masukkan lebar balok ' + str(x) + ' : '))
    t = int(input('Masukkan tinggi balok ' + str(x) + ' : '))
    v = p*l*t
    volume.append(v)
print('volume terbesar balok adalah : ' ,max(volume))

N = int(input('Masukkan N : '))
x = 1
for i in range(N):
    p = int(input('Masukkan panjang balok ' + str(x) + ' : '))
    l = int(input('Masukkan lebar balok ' + str(x) + ' : '))
    t = int(input('Masukkan tinggi balok ' + str(x) + ' : '))
    v = p*l*t
    x += 1
print('volume terbesar balok adalah : ' ,max(v))
