import operator

N = int(input())
lst=[]
for i in range(N) : 
    word = input()
    lst.append((len(word), word))
lst = list(set(lst))
lst.sort()

for i in lst :
    print(i[1])