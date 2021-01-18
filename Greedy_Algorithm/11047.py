<<<<<<< HEAD
n,k = map(int, input().split())
money=[]
count=0

for i in range(n) :
    money.append(int(input()))

for j in range(n-1, -1, -1) :
    if k!=0 :
        count += k//money[j]
        k=k%money[j]
=======
n,k = map(int, input().split())
money=[]
count=0

for i in range(n) :
    money.append(int(input()))

for j in range(n-1, -1, -1) :
    if k!=0 :
        count += k//money[j]
        k=k%money[j]
>>>>>>> 8a0a3a07728b30a5a301d170f090e0896e9ed10d
print(count)