F = float(input(('Masukkan suhu dalam Farenheit : ')))
C = (5 * F - 160)/9
R = (4 * F -128)/9
K =  (5 * F + 2297)/9

Kode = input('Masukkan Kode Suhu : ')
if Kode == 'C':
    Suhu = 'Celcius'
    Output = C
elif Kode == 'R':
    Suhu = 'Reamur'
    Output = R
elif Kode == 'K':
    Suhu = 'Kelvin'
    Output = R

print('Suhu dalam ' + Suhu + ' adalah ' + str(Output))

