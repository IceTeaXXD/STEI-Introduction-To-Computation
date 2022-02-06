# Hitung Nilai Tertinggi 
banyakSoal = int(input('Masukkan banyak soal : '))
kj = input('Kunci Jawaban : ')
banyakHasil = int(input('Masukkan banyak hasil ujian : '))
nilai = 0
nilaimax = -1000000000000000000000000000000000000
countNilai = 0

for i in range (banyakHasil):
    jawaban = input('Hasil ujian ke-' + str(i+1) + ' : ')
    for j in range (banyakSoal):
        print ('jawaban j :' ,jawaban[j])
        print ('kj : ', kj[j])
        if jawaban[j] == 'X' :
            nilai += 0
        elif jawaban[j] == kj [j]:
            nilai += 3
        elif jawaban[j] != kj [j]:
            nilai -= 1
        print('nilai :',nilai)

    if nilai > nilaimax:
        nilaimax = nilai 
        countNilai = 0
        print('nilai max : ',nilaimax)

    if nilai == nilaimax:
        countNilai += 1
    nilai = 0

print('Terdapat', countNilai, 'orang dengan nilai tertinggi',nilaimax)