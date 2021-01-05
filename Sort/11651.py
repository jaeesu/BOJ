N=int(input())
list=[]
for i in range(N) :
    x,y=map(int, input().split())
    list.append((y,x))
list.sort()

for i in list :
    print(i[1], i[0])