<<<<<<< HEAD
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

=======
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

>>>>>>> 8a0a3a07728b30a5a301d170f090e0896e9ed10d
summ(0,lst,N)