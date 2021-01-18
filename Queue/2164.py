<<<<<<< HEAD
#원형큐
import sys

def card(lst) :
    while(lst) :
        if(len(lst)==1) : 
            print(lst.pop())
            return
        del lst[0]
        lst.append(lst[0])
        del lst[0]

que=[]

N = int(input())
que=[i for i in range(1,N+1)]

=======
#원형큐
import sys

def card(lst) :
    while(lst) :
        if(len(lst)==1) : 
            print(lst.pop())
            return
        del lst[0]
        lst.append(lst[0])
        del lst[0]

que=[]

N = int(input())
que=[i for i in range(1,N+1)]

>>>>>>> 8a0a3a07728b30a5a301d170f090e0896e9ed10d
card(que)