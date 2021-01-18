from collections import Counter
import math

def mod(arr) :
    if(len(arr)==1) :
        return arr[0]
    else :
        cnt = Counter(arr).most_common()
        if(cnt[0][1]==cnt[1][1]) :
            return cnt[1][0]
        else :
            return cnt[0][0]


lst=[]
N=int(input())
for i in range(N) : lst.append(int(input()))
lst.sort()
print(round(sum(lst)/len(lst)))
print(lst[int((N-1)/2)])
print(mod(lst))
print(max(lst)-min(lst))