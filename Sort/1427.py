N = int(input())
list=[]
while(N!=0) :
    list.append(N%10)
    N=int(N/10)
list.sort(reverse=True)
for i in list :
    print(i,end='')