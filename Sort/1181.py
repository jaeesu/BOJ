<<<<<<< HEAD
import operator

N = int(input())
lst=[]
for i in range(N) : 
    word = input()
    lst.append((len(word), word))
lst = list(set(lst))
lst.sort()

for i in lst :
=======
import operator

N = int(input())
lst=[]
for i in range(N) : 
    word = input()
    lst.append((len(word), word))
lst = list(set(lst))
lst.sort()

for i in lst :
>>>>>>> 8a0a3a07728b30a5a301d170f090e0896e9ed10d
    print(i[1])