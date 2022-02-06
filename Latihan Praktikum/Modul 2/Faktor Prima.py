# Faktor Prima
N = int(input('Masukkan N : '))
print('Faktor primanya adalah ',end=" ")
for i in range(2, N+1):
    if N % i == 0:
        count = 1
        for j in range(2,(i//2 + 1)):
            if(i % j == 0):
                count = 0
                break
        if(count == 1):
            print(i,',',end=" ")

""" definisi = True
if N > 1:
    # Cek faktor yang bisa membagi x
    for i in range(2, N+1):
        if (N % i) == 0:
            # Jika memiliki modulo 0 atau tidak bisa dibagi dengan angka selain angka tersebut, maka bilangan prima
            # Looping ini untuk terus mencari pembagi bilangan x dari dengan range angka 2 sampai angka tersebut
            definisi = False

# Cek jika definisi merupakan boolean True
if definisi:
    print(N, end=" ")    """