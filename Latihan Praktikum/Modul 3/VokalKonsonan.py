# Cek Vokal dan Konsonan
N = int(input('Masukkan N : '))
string = input('Masukkan string : ')
vokal = 0
konsonan = 0
temp = 0

for i in range (N):
    if string[i] == 'a' or string[i] == 'i' or string[i] == 'u' or string[i] == 'e' or string[i] == 'o':
        vokal += 1
    elif string[i] == ' ':
        vokal += 0
    else :
        konsonan += 1

print('Terdapat',vokal,'huruf vokal dan',konsonan,'huruf konsonan')