number = int(input("Enter a number:"))
lst =[]
for i in range(2, number+1):
	if number % i == 0:
		lst.append(i)
print (lst)