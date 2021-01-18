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
    def size(self) :
        return len(self.lst)
    def empty(self) :
        if(len(self.lst)==0) :
            return 1
        return 0
    def top(self) :
        if(len(self.lst)==0) :
            return -1
        return self.lst[-1]

N = int(input())
lst_stack=stack()
for i in range(N) :
    lst=input().split()
    a=lst[0]
    if(a=="push") : lst_stack.push(lst[1])
    elif(a=="pop") : print(lst_stack.pop())
    elif(a=="size") : print(lst_stack.size())
    elif(a=="empty") : print(lst_stack.empty())
    elif(a=="top") : print(lst_stack.top())
