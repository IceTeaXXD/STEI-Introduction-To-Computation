def VKubus(s):
    Vol_Kubus = s ** 3
    return Vol_Kubus

def VLimas(s,t):
    Vol_Limas = (1/3) * (s ** 2) * t
    return Vol_Limas

s = int(input('Masukkan panjang sisi kubus: '))
t = int(input('Masukkan tinggi limas: '))

Vol_Kubus = VKubus(s)
Vol_Limas = VLimas(s,t)

Hasil = Vol_Kubus + Vol_Limas

print('Volume rumah yang terbentuk adalah ' + str(Hasil) + ' meter kubik.')