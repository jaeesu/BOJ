#최대공약수
def GCD(a,b) :
    if(a<b) : a,b=b,a
    while(b!=0) :
        a,b=b,a%b
    return int(a)

#최소공배수
def LCM(a,b) : 
    return int(a*b/GCD(a,b))

N,M = map(int, input().split())
print(GCD(N,M))
print(LCM(N,M))