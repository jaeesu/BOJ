# counting sort : 계수 정렬

import sys
N = int(input())

arr = [0]*10001

for i in range(N) :
    arr[int(sys.stdin.readline())] += 1
    
for i in range(len(arr)) :
    while(arr[i]!=0) :
        print(i)
        arr[i]-=1
