def reverseSentence():
    ask = input("Enter your sentence: ")
    reverseList = []
    if len(ask) > 1:
        result =  ask.split()
        result =  result[::-1]
        final = " ".join(result)
        return final

print(reverseSentence())
