N = int(input())

arr=[]

for i in range(N) :
    arr.append(int(input()))

arr.sort()

for i in arr :
    print(i)

'''
v=[int(input()) for i in range(int(input()))]
print("\n".join(map(str, sorted(v))))
'''