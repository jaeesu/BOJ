#max_heap###
import sys
import heapq as heap

n=int(sys.stdin.readline())
lst=[]
for i in range(n) :
    x = int(sys.stdin.readline())
    heap.heappush(lst, (-x,x))
    if(x==0) :
        if len(lst) > 0 :
            print(heap.heappop(lst)[1])
        else :
            print(0)