import random
print(" Welcome to the Cows and Bulls Game! ")
def compare_numbers(number, guess_number):
    cowbull = [0,0]
    numberList = list(number)
    guess_numberList = list(guess_number)
    for j in numberList:
        if j in guess_numberList:
            for i in range(len(number)):
                if number[i] == guess_number[i]:
                    cowbull[0] += 1
                else:
                    cowbull[1] += 1
        else:
        	cowbull = [0,0]
    return cowbull
	

if __name__=="__main__":
    playing = True
    number = str(random.randint(1000, 9999))
    guesses = 0

while playing:
    guess_number =input("Enter Your 4-digit Number:")
    if guess_number == "exit":
        break
    cowbull_count = compare_numbers(number, guess_number)

    print(str(cowbull_count[0]) + "cows, " + str(cowbull_count[1]) + "bulls")

    if cowbull_count[0] == 4:
        playing = False
        print(guess_number, "4 bulls!")
        break
    else:
        print("Keep trying!")
        print(number)

