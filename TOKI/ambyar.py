data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
m = [13,17,25,28,30,41,45,56,58,64,73,76,87,91,98]
n = 15
a = 1
b = n
f = 98
ambyar = 0
while a<=b:
    m = (a+b) / 2
    ambyar = ambyar + data[m]
    if data[m] == f:
        break
    elif data[m] < f:
        a = m+1
    else:
        b = m-1

print(ambyar)
        