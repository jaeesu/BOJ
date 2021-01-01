def quadrant(x,y) :
    if (x>0) :
        if (y>0) :return 1
        else : return 4
    else :
        if(y>0) : return 2
        else : return 3

a,b = input().split()

'''while(int(a) * int(b) == 0) :
    a,b = input().split()'''

print(quadrant(int(a),int(b)))