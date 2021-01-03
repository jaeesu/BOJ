visited = [False]*9
out, out_all = [], []

def finder(cnt, N, M) :
    if cnt==M :
        out_str = (' '.join(map(str, sorted(out))))
        if out_str not in out_all :
            out_all.append(out_str)
        return
    for i in range(N) :
        if not visited[i] :
            visited[i] = True
            out.append(i+1)
            finder(cnt+1, N, M)
            visited[i] = False
            out.pop()

N,M=map(int, input().split())
finder(0, N, M)

for i in out_all :
    print(i)