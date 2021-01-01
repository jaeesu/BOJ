'''TRUE=True
FALSE=False

a,b=input().split()
a=int(a)
b=int(b)

while(a>8 or a<b or b<1) :
    a,b=input().split()
    a=int(a)
    b=int(b)


visited[b]=[]

def recur(a,b) :
    for i in int(b) :
        if(visited[i]==FALSE) :
            visited[i] = TRUE
            cnt=cnt+1'''