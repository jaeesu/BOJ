def star(i,j,nu) : 
    if((i/nu)%3==1 and (j/nu)%3==1) :
        print(" ",end='')
    else :
        if(nu/3==0) :
            print("*",end='')
        else :
            star(i,j,nu/3)

N=int(input())
for i in range(N) : 
    for j in range(N) :
        star(i,j,N)
    print("\n")