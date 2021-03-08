def binary_search() :
    left=0
    right=N-1  
    while(right>=left):
        mid = int((left+right)/2)
        if(compared[_]<standard[mid]) : right = mid-1
        elif(compared[_]>standard[mid]) : left = mid+1
        elif(compared[_]==standard[mid]) : 
            print("1")
            return
    print("0")


standard = []
compared = []

#배열 인덱스 N 입력
N = int(input())
#배열의 수 N개 입력
standard = input().split()
standard.sort()
#비교값 M 입력
M = int(input())
#비교값 M개 입력
compared = input().split()
#존재하면 1, 아니면 0 출력
#-left, right, mid 설정
#-mid보다 큰 경우 left = mid+1, 작은 경우 right = mid-1

for _ in range(M): binary_search()