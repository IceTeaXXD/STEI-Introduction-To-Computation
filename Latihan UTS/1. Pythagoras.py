def radit():
    a = float(input('Masukkan a : '))
    b = float(input('Masukkan b : '))
    return a,b

def kelvin(a,b):
    miring = ((a**2) + (b**2)) ** (1/2)
    return miring

def justin(miring):
    print('Sisi miring adalah',miring)
    return

a,b = radit()
miring = kelvin(a,b)
justin(miring)
