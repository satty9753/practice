import random
a = [random.randrange(1,50,1) for i in range(1,20)]
b = [random.randrange(1,50,1) for i in range(1,20)]
c = [element for element in set(a) if element in b]
print (a)
print (b)
print (c)
