def masuk():
    x = int(input('Masukkan X : '))
    y = int(input('Masukkan Y : '))
    return x,y

def cek(x,y):
    if x > 0 and y > 0:
        kuadran = 1
    elif x < 0 and y > 0 :
        kuadran = 2
    elif x < 0 and y < 0 :
        kuadran = 3
    elif x > 0 and  y < 0 :
        kuadran = 4
    else : 
        kuadran = 0
    return kuadran

def keluar(kuadran):
    if kuadran > 0:
        print('P terletak di kuadran',kuadran)
    else : 
        print('Kuadran tidak bisa dihitung')
    return

x,y = masuk()
kuadran = cek(x,y) 
keluar(kuadran)