<<<<<<< HEAD
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
=======
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
>>>>>>> 8a0a3a07728b30a5a301d170f090e0896e9ed10d
    print(check(lst_stack))