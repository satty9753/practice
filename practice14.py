import random
def listRemoveDuplicate():
    randomList = [random.randrange(1,50,1) for i in range(1, 20)]
    newList = set(randomList)
    return newList
print(listRemoveDuplicate())

