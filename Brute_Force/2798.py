vst=[0]*100
chk=[0]*(100*99*98)

def summ(cnt, arr, A) :
    if cnt==3 :
        print(chk)
        return

    for i in arr :
        if not vst[i] :
            vst[i] = True
            chk.append(i)
            summ(cnt+1, N, M)
            chk.pop()
            vst[i] = False

N, M=map(int, input().split())
lst=list(map(int, input().split()))

summ(0,lst,N)