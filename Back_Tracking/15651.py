visited = [False]*9
out=[]

def finder(cnt, N, M) :
    if cnt==M :
        print(' '.join(map(str, out)))
        return
    for i in range(N) :
        out.append(i+1)
        finder(cnt+1, N, M)
        out.pop()

N,M=map(int, input().split())
finder(0, N, M)

'''visited = [False]*9
out=[]

def finder(cnt, N, M) :
    if cnt==M :
        print(' '.join(map(str, out)))
        return
    for i in range(N) :
        if not visited[i] :
            visited[i] = True
            out.append(i+1)
            visited[i] = False
            finder(cnt+1, N, M)
            out.pop()

N,M=map(int, input().split())
finder(0, N, M)'''