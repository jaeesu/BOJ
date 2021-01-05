from collections import Counter
import math

def mod(arr) :
    if(len(arr)==1) :
        return arr[0]
    else :
        cnt = Counter(list).most_common()
        if(cnt[0][1]==cnt[1][1]) :
            return cnt[1][0]
        else :
            return cnt[0][0]


list=[]
N=int(input())
for i in range(N) : list.append(int(input()))
list.sort()
print(round(sum(list)/len(list)))
print(list[int((N-1)/2)])
print(mod(list))
print(max(list)-min(list))