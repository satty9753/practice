import random
def generatePassword():
    azLowercase = "abcdefghijklomnopqrstuvwxyz"
    azUppercase = azLowercase.upper()
    azLowercase =  list(azLowercase)
    azUppercase =  list(azUppercase)
    symbols = "!@#$%^&*()"
    symbols =  list(symbols)
    numbers = "0123456789"
    numbers = list(numbers)
    total = azLowercase + azUppercase + symbols + numbers
    passwordList = [random.choice(total) for i in range(random.randint(6, 16))]
    password = "".join(passwordList)
    return password
print(generatePassword())
print(generatePassword())
print(generatePassword())