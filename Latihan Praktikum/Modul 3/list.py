N = int(input('Masukkan nilai N : '))
K = int(input('Masukkan nilai K : '))
Tab = [0 for i in range(N)]
cek = True
count = 0
total = 0
x = 2

for i in range (N):
    Tab[i] = int(input('Masukkan bilangan ke-' + str(i+1) + ' : '))

for i in range(N):
    hasil = Tab[i] + Tab[i+1]
    while cek == True: 
        if hasil % K == 0:
            count += 1
            hasil += Tab[i+x]
        elif hasil % K != 0:
            cek == False
        x += 1
    if count > 0:
        total += 1
    hasil = 0
if total > 0:
    print('Terdapat',total,'potongan list yang jumlahnya habis dibagi',K)
elif total == 0:
    print('Tidak ada potongan list yang memenuhi')
            
