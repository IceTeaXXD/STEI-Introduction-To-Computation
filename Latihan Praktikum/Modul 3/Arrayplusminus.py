E = int(input("Masukkan banyak elemen: "))
listE = [0 for i in range(E)]
newList = [0 for i in range(E)]

for i in range (E):
    listE[i] = int(input("Masukkan elemen ke-" + str(i+1) + ": "))

for i in range(E):
    if listE[i] < listE[i-1]:
        newList[i] = listE[i] + listE[i-1]
    elif listE[i] > listE[i-1]:
        newList[i] = listE[i] - listE[i-1]
    else:
        newList[i] = listE[i]
    print(newList)

print([listE])
print([newList])

print("Hasil akhir: ")
for i in range (E):
    print (newList[i],end=' ')