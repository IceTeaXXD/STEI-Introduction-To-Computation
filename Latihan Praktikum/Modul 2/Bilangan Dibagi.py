N = int(input('Masukkan bilangan N : '))
x = 0
while N > 1: 
    if N % 2 == 0:
        N = N // 2
        x += 1
    else : 
        N -= 1
        x += 1

print('Banyak langkah yang diperlukan adalah',x)