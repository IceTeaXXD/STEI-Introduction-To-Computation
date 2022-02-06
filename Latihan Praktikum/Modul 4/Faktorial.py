N = int(input('Masukkan panjang string: '))
kata = input('Masukkan string: ')

atas = 1
count = 1
bawah = 1

for i in range (1,N+1):
    atas *= i

for i in range (N):
    for j in range(N):
        if kata[i] == kata[j]:
            count += 1
    print ('count : ',count)
    for z in range(1,count):
        bawah *= z
    count = 1

print(atas,bawah)
hasil = atas / bawah
print('hasil : ',hasil)