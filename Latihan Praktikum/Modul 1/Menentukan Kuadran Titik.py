# NIM/Nama : 16521516/Ahmad Nadil
# Tanggal  : 3 Oktober 2021
# Deskripsi : Penentuan Kuadran

X = int(input('Masukkan nilai X : '))
Y = int(input('Masukkan nilai Y : '))

if X > 0 and Y > 0: 
    print('(' + str(X) + ',' +str(Y) + ') ' + 'ada di kuadran 1')
elif X < 0 and Y > 0:
    print('(' + str(X) + ',' +str(Y) + ') ' + 'ada di kuadran 2')
elif X < 0 and Y < 0:
    print('(' + str(X) + ',' +str(Y) + ') ' + 'ada di kuadran 3')
elif X > 0 and Y < 0:
    print('(' + str(X) + ',' +str(Y) + ') ' + 'ada di kuadran 4')
elif X == 0 and Y != 0:
    print('(' + str(X) + ',' +str(Y) + ') ' + 'ada di sumbu Y')
elif Y == 0 and X != 0:
    print('(' + str(X) + ',' +str(Y) + ') ' + 'ada di sumbu X')
elif X == 0 and Y == 0:
    print('(' + str(X) + ',' +str(Y) + ') ' + 'ada di titik pusat')
else :
    print('Input yang anda masukkan salah')
    print('Silakan ulangi program')