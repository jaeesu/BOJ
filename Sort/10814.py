<<<<<<< HEAD
N = int(input())
lst=[]
for i in range(N) :
    x,y = input().split()
    lst.append((len(x), x, i, y))

lst.sort()
for i in lst:
=======
N = int(input())
lst=[]
for i in range(N) :
    x,y = input().split()
    lst.append((len(x), x, i, y))

lst.sort()
for i in lst:
>>>>>>> 8a0a3a07728b30a5a301d170f090e0896e9ed10d
    print(i[1], i[3])