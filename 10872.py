def fac(num) :
    if num==1 :
        return 1
    elif num==0 :
        return 0
    return num*fac(num-1)

N = input()
print(fac(N))