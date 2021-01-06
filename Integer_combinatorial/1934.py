set=int(input())

for i in range(set) :
    N,M = map(int, input().split())
    mult=N*M
    if(N<M) : N,M=M,N
    while(M!=0) :
        N,M=M,N%M
    print(int(mult/N))