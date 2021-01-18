def fac(nu) :
    if(nu==0) : return 1
    elif(nu==1) : return 1
    else : return nu*fac(nu-1) 

N = int(input())
print(fac(N))