class Deque:
    def __init__(self) :
        self.deq=[]
    def push(self, num) :
        self.deq.append(num)
    def pop(self) :
        temp=self.deq[0]
        del self.deq[0]
        return temp

deq=Deque()

N,K=map(int, input().split())

for i in range(N) : 
    deq.push(i+1)

print("<", end="")

for i in range(int((N-1)/2)) :
    for j in range(K-1) :
        deq.push(deq.pop())
        deq.push(deq.pop())
        print(deq.pop(), end=", ")
print(deq.pop(), end=">")
