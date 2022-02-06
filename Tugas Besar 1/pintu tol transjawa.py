def pintu_tol(a,b):
    harga=[0,44000,7500,15000,15000,107500,12000,29000,57500,39000,75000,5000,65000,91000,88000,49000,38000,4500,36000,26500]
    total=0
    if a<b:
        for i in range (a,b):
            total=total+harga[i]
    else:
        
        for i in range (b,a):
            total=total+harga[i]
    return total

print('1. Merak')
print('2. Tangerang')
print('3. JORR')
print('4. Jakarta')
print('5. Cikampek')
print('6. Palimanan')
print('7. Kanci')
print('8. Pejagan')
print('9. Pemalang')
print('10. Batang')
print('11. Semarang')
print('12. Semarang ABC')
print('13. Solo')
print('14. Ngawi')
print('15. Kertosono')
print('16. Mojokerto')
print('17. Surabaya')
print('18. Gempol')
print('19. Pasuruan')
print('20. Probolinggo')

masuk=int(input('Masukkan Pintu Masuk Tol: '))
keluar=int(input('Masukkan Pintu Keluar Tol: '))
x=pintu_tol(masuk,keluar)
print('Total yang harus anda bayar sebesar Rp.',x)




