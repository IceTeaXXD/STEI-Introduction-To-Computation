# Poin Awal (Kemenangan)
poinRic = 0
poinDip = 0
poinKil = 0

print('Pertandingan Tim Ric vs Tim Dip')
Ric1 = int(input('Banyak bola yang dimasukkan Tim Ric : '))
Dip1 = int(input('Banyak bola yang dimasukkan Tim Dip : '))
if Ric1 > Dip1 :
    poinRic += 1
elif Ric1 == Dip1:
    poinRic += 1
    poinDip += 1
else : 
    poinDip += 1
 
print('Pertandingan Tim Ric vs Tim Kil')
Ric2 = int(input('Banyak bola yang dimasukkan Tim Ric : '))
Kil1 = int(input('Banyak bola yang dimasukkan Tim Kil : '))
if Ric2 > Kil1:
    poinRic += 1
elif Ric2 == Kil1:
    poinRic += 1
    poinKil += 1
else :
    poinKil += 1

print('Pertandingan Tim Dip vs Tim Kil')
Dip2 = int(input('Banyak bola yang dimasukkan Tim Dip : '))
Kil2 = int(input('Banyak bola yang dimasukkan Tim Kil : '))
if Dip2 > Kil2:
    poinDip += 1
elif Dip2 == Kil2:
    poinDip += 1
    poinKil += 1
else : 
    poinKil += 1

skorDip = (Dip1 - Ric1) + (Dip2 - Kil2)
skorKil = (Kil1 - Ric2) + (Kil2 - Dip2)
skorRic = (Ric1 - Dip1) + (Ric2 - Kil1)


if poinDip > poinKil and poinDip > poinRic:
    print('Tim Dip yang memenangkan lomba')
elif poinRic > poinDip and poinRic > poinKil:
    print('Tim Ric yang memenangkan lomba')
elif poinKil > poinDip and poinKil > poinRic : 
    print('Tim Kil yang memenangkan pertandingan')
else : 
    if skorDip > skorKil and skorDip > skorRic:
        print('Tim Dip yang memenangkan lomba')
    elif skorRic > skorDip and skorRic > skorKil:
        print('Tim Ric yang memenangkan lomba')
    elif skorKil > skorDip and skorKil > skorRic:
        print('Tim Kil yang memenangkan pertandingan')
    else : 
        print('Tidak ada yang memenangkan lomba tersebut')


