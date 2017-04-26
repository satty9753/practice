import random
a = [random.randrange(0,50,1) for i in range(1,50)]
b = [random.randrange(0,50,1) for i in range(1,50)]
lst = []
for i in a:
    if i in b and i not in lst:
 	   lst.append(i)
print (a)
print (b)
print (lst)