<<<<<<< HEAD
N = int(input())

arr=[]

for i in range(N) :
    arr.append(int(input()))

for i in range(N) :
    for j in range(i,N) :
        if(arr[i]>arr[j]) :
            arr[i], arr[j] = arr[j], arr[i]


for i in arr :
=======
N = int(input())

arr=[]

for i in range(N) :
    arr.append(int(input()))

for i in range(N) :
    for j in range(i,N) :
        if(arr[i]>arr[j]) :
            arr[i], arr[j] = arr[j], arr[i]


for i in arr :
>>>>>>> 8a0a3a07728b30a5a301d170f090e0896e9ed10d
    print(i)