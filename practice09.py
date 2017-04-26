import random
lst = []
while True:
	question = input("Guess a number between 1 to 9:")
	randomNumber = random.randrange(1,9,1)
	lst.append(question)
	if question == "exit()":
		break
	elif int(question) == randomNumber:
	    print(question, "Exactly right!") 
	elif int(question) > randomNumber:
	    print("Too high!")
	elif int(question) < randomNumber:
	    print("Too low!")
	else:
		print("Please try again.")
print (len(lst), lst)
