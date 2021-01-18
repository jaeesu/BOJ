<<<<<<< HEAD
import sys
input=sys.stdin.readline

class stack :
    def __init__(self) :
        self.lst=[]
    def push(self, data) :
        self.lst.append(data)
    def pop(self) :
        if(len(self.lst)==0) :
            return -1
        return self.lst.pop()
    def sum(self) :
        return(sum(self.lst))


N = int(input())
lst_stack=stack()
for i in range(N) :
    a=int(input())
    if(a==0) : lst_stack.pop()
    else : lst_stack.push(a)

=======
import sys
input=sys.stdin.readline

class stack :
    def __init__(self) :
        self.lst=[]
    def push(self, data) :
        self.lst.append(data)
    def pop(self) :
        if(len(self.lst)==0) :
            return -1
        return self.lst.pop()
    def sum(self) :
        return(sum(self.lst))


N = int(input())
lst_stack=stack()
for i in range(N) :
    a=int(input())
    if(a==0) : lst_stack.pop()
    else : lst_stack.push(a)

>>>>>>> 8a0a3a07728b30a5a301d170f090e0896e9ed10d
print(lst_stack.sum())