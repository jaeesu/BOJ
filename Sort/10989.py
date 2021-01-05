# counting sort : 계수 정렬

import sys
N = int(sys.stdin.readline())

arr = [0]*10001

for i in range(N) :
    arr[int(sys.stdin.readline())] += 1
    
print("-------------------")
for i in range(len(arr)) :
    while(arr[i]!=0) :
        print(i)
        arr[i]-=1
