n,k = map(int, input().split())
money=[]
count=0

for i in range(n) :
    money.append(int(input()))

for j in range(n-1, -1, -1) :
    if k!=0 :
        count += k//money[j]
        k=k%money[j]
print(count)