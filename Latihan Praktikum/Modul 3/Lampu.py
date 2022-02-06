# Mati Nyalain Lampu
N = int(input('Masukkan banyak lampu : '))
Lampu = [0 for i in range(N)]

print(Lampu)

X = int(input('Masukkan berapa kali Tuan Kil menekan tombol : '))

for y in range (X):
    tombol = int(input('Tombol yang akan ditekan ke ' + str(y+1) + ' : '))
    if Lampu[tombol-1] == 0:
        Lampu[tombol-1] += 1
    elif Lampu[tombol-1] == 1:
        Lampu [tombol-1] -= 1

    if tombol-1 == 0 :
        if Lampu[1] == 0:
            Lampu[1] += 1
        elif Lampu[1] == 1:
            Lampu[1] -= 1

    elif tombol-1 == N-1:
        if Lampu[N-2] == 0:
            Lampu[N-2] += 1
        elif Lampu[N-2] == 1:
            Lampu[N-2] -= 1
        
    else : 
        if Lampu[(tombol-1) - 1] == 0:
            Lampu[(tombol-1) - 1] += 1
        elif Lampu[(tombol-1) - 1] == 1:
            Lampu[(tombol-1) - 1] -= 1
            
        if Lampu[(tombol-1) + 1] == 0:
            Lampu[(tombol-1) + 1] += 1
        elif Lampu[(tombol-1) + 1] == 1:
            Lampu[(tombol-1) + 1] -= 1
    print (Lampu)

print('Keadaan akhir rangkaian lampu adalah',end=" ")
for j in range (N):
    print(Lampu[j],end='')