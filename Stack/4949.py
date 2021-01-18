import sys

def check(word, lst) :
    if(word=="(" or word=="[") :
        lst.append(word)
    elif(word==")") :
        if (len(lst)<=0 or lst[-1]!="(") :
            return False
        lst.pop()
    elif(word=="]") :
        if (len(lst)<=0 or lst[-1] != "[") :
            return False
        lst.pop()
    return True

while(1) :
    global stk
    stk=[]
    line=sys.stdin.readline().rstrip()
    if(line==".") : break
    for word in line :
        if(word==".") : 
            if(check(word,stk)==True) :
                print("yes")
                break
        if (check(word, stk)==False) :
            print("no")
            break
