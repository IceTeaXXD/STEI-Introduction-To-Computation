""" # Love w/ while
y = 15
while y >= -15:
    for x in range(-30, 31):
        rumus = ((x / 2) ** 2) + (((5 * y / 4) - 2 * (abs(x) ** (1/2))) ** 2)
        if abs(rumus) <= 120:
            print("*", end="")
        else:
            print(end=" ")
    y -= 1
    print()

# Love w/ for
for y in range (15,-16,-1):
    for x in range(-30, 31):
        rumus = ((x / 2) ** 2) + (((5 * y / 4) - 2 * (abs(x) ** (1/2))) ** 2)
        if abs(rumus) <= 120:
            print("*", end="")
        else:
            print(end=" ")
    print()

# Better Love
for y in range(30,-31,-1):
    for x in range(-60,61):
        f = (((x/2)**2 + (5*y/4 -2*(abs(x)**0.5))**2)/2)
        if f <= 120:
            print("*", end="")
        else : print(end=" ")
    print()

# Sapiq Homo
s = 'SAPIQHOMO'
a = 9
b = 3
ind = 0
#atas
for i in range(b,-1,-1):
  for x in range(2):
    for j in range(i):
      print(end=' ')
    for j in range(a):
      print(s[ind], end='')
      ind = (ind+1)%9
    if (x == 0):
      for j in range(i):
        print(end=' ')
  a += 2
  print()
a = 15
#bawah
b = 0
while(a > 0):
  for i in range(b):
    print(end=' ')
  for i in range(2*a):
    print(s[ind], end='')
    ind = (ind+1)%9
  print()
  a -= 1
  b += 1 """

# Love Input
s = input('Masukkan Text : ')
a = 9
b = 3
ind = 0
#atas
for i in range(b,-1,-1):
  for x in range(2):
    for j in range(i):
      print(end=' ')
    for j in range(a):
      print(s[ind], end='')
      ind = (ind+1)%len(s)
    if (x == 0):
      for j in range(i):
        print(end=' ')
  a += 2
  print()
a = 15
#bawah
b = 0
while(a > 0):
  for i in range(b):
    print(end=' ')
  for i in range(2*a):
    print(s[ind], end='')
    ind = (ind+1)%len(s)
  print()
  a -= 1
  b += 1