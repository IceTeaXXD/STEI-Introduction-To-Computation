a = int(input('Masukkan jumlah baris matriks: '))
b = int(input('Masukkan jumlah kolom matriks: '))
Array = [[0 for j in range(b)] for i in range(a)] 
for i in range (a):
    for j in range(b):
        Array[i][j] = int(input('Masukkan elemen baris ' + str(i+1) + ' kolom ' + str(j+1) +' : '))
print(Array)
