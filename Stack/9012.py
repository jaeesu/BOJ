import sys
input=sys.stdin.readline

def check(lst) :
    del lst[len(lst)-1]
    num=0
    while(len(lst)!=0) :
        if lst[-1]=='(' :
            num-=1
            if num<0 : return ('NO')
        else :
            num+=1
        del lst[len(lst)-1]

    if(num>0) : return ('NO')
    return ('YES')


N = int(input())

for i in range(N) :
    lst_stack=list(input())
    print(check(lst_stack))