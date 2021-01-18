def fibo(nu) :
    if(nu==0) : return 0
    elif(nu==1) : return 1
    else : return fibo(nu-1) + fibo(nu-2)

N=int(input())
print(fibo(N))