with open("primenumbers.txt") as f1:
	line1 = f1.readlines()
with open("happynumbers.txt") as f2:
	line2 = f2.readlines()
s = set(line2)
line3 = [i for i in line1 if i not in s]
for x in line3:
    x = x.strip()
    print(x)