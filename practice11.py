num = int(input("Enter your number:"))
a = [i for i in range(2, num+1) if num % i == 0]
def isPrime(n):
    if num > 1:
        if len(a) == 1:
            print("prime number")
        else:
            print("Not a prime number")
    else:
        print("Not a prime number") 

isPrime(num)