# Menghitung Bilangan Tertinggi Dalam Piramida

# input n dan elemen array
n = int(input("Masukkan bilangan N: "))
arr = [int(input("Masukkan bilangan ke "+ str(i+1) +": ")) for i in range(n)]

# perulangan bersarang untuk menentukan bilangan di puncak piramida
for i in range(n):
    for j in range(n-1-i):
        arr[j] += arr[j+1]
        
# output hasil
print("Bilangan di puncak piramida adalah " + str(arr[0]))