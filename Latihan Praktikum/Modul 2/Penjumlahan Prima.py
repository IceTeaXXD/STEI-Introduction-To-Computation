""" N = int(input("Insert number : "))  
x = 0
for num in range(N):  
    if num > 1:  
        for i in range(2,num):  
           if (num % i) == 0:  
               break  
        else:  
            for j in range(num):
                if j + num == N:
                    print(j,'+',num)
                    x += 1
if x > 0:
    print('There are',x,'pairs that satisfies')
else : 
    print('There is no pair that satisfies') """

N = int(input("Insert number : "))  
x = 0
for num in range(N):  
    if num > 1:  
        for i in range(2,num):  
            if (num % i) == 0:  
               break  
        else:  
            for j in range(num):
                for z in range(2,j):
                    if (j%z) == 0:
                        break
                else: 
                    if j + num == N:
                        print(j,'+',num)
                        x += 1
if x > 0:
    print('There are',x,'pairs that satisfies')
else : 
    print('There is no pair that satisfies') 