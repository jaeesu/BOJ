N=int(input())
list=[]
for i in range(N) :
    x,y=map(int, input().split())
    list.append((x,y))
list = sorted(list)

for i in list :
    print(i[0], i[1])