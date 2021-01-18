<<<<<<< HEAD
import sys

class Queue :
    def __init__(self) :
        self.queue=[]
    def push(self, num) :
        self.queue.append(num)
    def pop(self) :
        if(len(self.queue)==0) : return -1
        else : 
            temp=self.queue[0]
            del self.queue[0]
            return temp
    def size(self) : 
        return len(self.queue)
    def empty(self) :
        if(len(self.queue)==0) : return 1
        return 0
    def front(self) :
        if(len(self.queue)==0) : return -1
        return self.queue[0]
    def back(self) :
        if(len(self.queue)==0) : return -1
        return self.queue[-1]

que=Queue()
N = int(sys.stdin.readline())

for i in range(N) : 
    line=sys.stdin.readline().split()
    a=line[0]
    if(a=="push") : que.push(line[1])
    elif(a=="pop") : print(que.pop())
    elif(a=="size") : print(que.size())
    elif(a=="empty") : print(que.empty())
    elif(a=="front") : print(que.front())
    elif(a=="back") : print(que.back())
=======
import sys

class Queue :
    def __init__(self) :
        self.queue=[]
    def push(self, num) :
        self.queue.append(num)
    def pop(self) :
        if(len(self.queue)==0) : return -1
        else : 
            temp=self.queue[0]
            del self.queue[0]
            return temp
    def size(self) : 
        return len(self.queue)
    def empty(self) :
        if(len(self.queue)==0) : return 1
        return 0
    def front(self) :
        if(len(self.queue)==0) : return -1
        return self.queue[0]
    def back(self) :
        if(len(self.queue)==0) : return -1
        return self.queue[-1]

que=Queue()
N = int(sys.stdin.readline())

for i in range(N) : 
    line=sys.stdin.readline().split()
    a=line[0]
    if(a=="push") : que.push(line[1])
    elif(a=="pop") : print(que.pop())
    elif(a=="size") : print(que.size())
    elif(a=="empty") : print(que.empty())
    elif(a=="front") : print(que.front())
    elif(a=="back") : print(que.back())
>>>>>>> 8a0a3a07728b30a5a301d170f090e0896e9ed10d
