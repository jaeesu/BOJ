<<<<<<< HEAD
N = int(input())
lst=[]
while(N!=0) :
    lst.append(N%10)
    N=int(N/10)
lst.sort(reverse=True)
for i in lst :
=======
N = int(input())
lst=[]
while(N!=0) :
    lst.append(N%10)
    N=int(N/10)
lst.sort(reverse=True)
for i in lst :
>>>>>>> 8a0a3a07728b30a5a301d170f090e0896e9ed10d
    print(i,end='')