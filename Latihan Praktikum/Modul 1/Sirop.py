A = int(input("Tentukan nilai A: "))
B = int(input("Tentukan nilai B: "))
C = int(input("Tentukan nilai C: "))
soda = int(input("Banyaknya soda: "))
susu = int(input("Banyaknya susu: "))
sirop = int(input("Banyaknya sirop: "))

so = soda//A
su = susu//B
si = sirop//C

if so <= su and so <= si:
    suso = so
elif su <= so and su <= si:
    suso = su
elif si <= so and si <= su:
    suso = si

print(suso * (A+B+C))