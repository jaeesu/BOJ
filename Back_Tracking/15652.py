<<<<<<< HEAD
visited = [False]*9
out=[]

def finder(cnt, win, N, M) :
    if cnt==M :
        print(' '.join(map(str, out)))
        return
    for i in range(win, N) :
        out.append(i+1)
        finder(cnt+1, i, N, M)
        out.pop()

N,M=map(int, input().split())
=======
visited = [False]*9
out=[]

def finder(cnt, win, N, M) :
    if cnt==M :
        print(' '.join(map(str, out)))
        return
    for i in range(win, N) :
        out.append(i+1)
        finder(cnt+1, i, N, M)
        out.pop()

N,M=map(int, input().split())
>>>>>>> 8a0a3a07728b30a5a301d170f090e0896e9ed10d
finder(0, 0, N, M)