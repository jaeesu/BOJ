N = int(input())
lst=[]
while(N!=0) :
    lst.append(N%10)
    N=int(N/10)
lst.sort(reverse=True)
for i in lst :
    print(i,end='')