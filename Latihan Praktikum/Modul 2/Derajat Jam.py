n=int(input('Masukkan Derajat : '))
sudutj=0 
sudutm=0
sudut=0
for j in range(12):
    for m in range(60):
        sudut=abs(((j * 30 + m * 0.5) - (m * 6))//1)
        if 360-sudut < sudut:
            sudut=360-sudut
        if sudut==n: print('%02d'%j+'.'+'%02d'%m)