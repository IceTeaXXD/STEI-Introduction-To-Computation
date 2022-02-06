def masuk():
    tc = float(input('Masukkan suhu (C) : '))
    kode = input('Kode Konversi (F/R/K) : ')
    return tc,kode

def Fahrenheit(tc):
    F = ((9/5) * tc) + 32
    satuan = 'Fahrenheit'
    return F,satuan

def Reamur(tc):
    R = (4/5) * tc
    satuan = 'Reamur'
    return R,satuan

def Kelvin (tc):
    K = tc + 273
    satuan = 'Kelvin'
    return K,satuan

def outputan (hasil,satuan):
    print('Konversi',tc,'celcius ke dalam',satuan,'adalah',hasil)



tc,kode = masuk ()

if kode == 'F':
    hasil,satuan = Fahrenheit(tc)
elif kode == 'R':
    hasil,satuan = Reamur(tc)
elif kode == 'K':
    hasil,satuan = Kelvin(tc)

outputan(hasil,satuan)