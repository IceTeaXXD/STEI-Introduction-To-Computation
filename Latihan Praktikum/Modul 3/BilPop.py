N = int(input('Masukkan banyak bilangan : '))
Tab = [0 for i in range(N)]
count = 0
populer = 0
for i in range (N):
    Tab[i] = int(input('Masukkan nilai bilangan ke-' + str(i+1) + ' : '))
for i in range (N):
    for j in range(N):
        for k in range(N):
            if Tab[i] == Tab[j] + Tab[k]:
                count += 1
    if count > 1:
        populer += 1
    count = 0
if populer > 0:
    print('Terdapat',populer,'bilangan Populer')
else : 
    print('Tidak terdapat bilangan populer')