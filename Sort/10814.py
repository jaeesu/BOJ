N = int(input())
lst=[]
for i in range(N) :
    x,y = input().split()
    lst.append((len(x), x, i, y))

lst.sort()
for i in lst:
    print(i[1], i[3])