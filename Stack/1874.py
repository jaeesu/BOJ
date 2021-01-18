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


N = int(input())
f_stack=stack()
s_stack=stack()
