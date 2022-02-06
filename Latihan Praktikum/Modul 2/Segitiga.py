# Bikin Segitiga
N = int(input('Masukkan N :'))
tinggi = N
while tinggi >= 1:
    spasi = N
    while spasi > tinggi:
        # display space
        print(' ', end=' ')
        spasi -= 1
    isi = 1
    while isi <= tinggi:
        print('*', end=' ')
        isi += 1
    print()
    tinggi -= 1