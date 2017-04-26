import random
def whetherInList():
    lst = list(range(21))
    random_number = random.randint(1, 100)
    if random_number in lst:
           print("Bingo")
    else:
            print(random_number, "X!")

whetherInList()