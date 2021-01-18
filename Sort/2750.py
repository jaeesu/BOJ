N = int(input())

arr=[]

for i in range(N) :
    arr.append(int(input()))

for i in range(N) :
    for j in range(i,N) :
        if(arr[i]>arr[j]) :
            arr[i], arr[j] = arr[j], arr[i]


for i in arr :
    print(i)