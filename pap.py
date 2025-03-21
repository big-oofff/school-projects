fhand = open("PrideandPrejudice.txt")
d = {"elizabeth": 0, "darcy": 0, "jane": 0, "bingley": 0}
for line in fhand:
    line = line.lower().split()
    print(line)
    for word in line:
        for c in d:
            if c in word:
                d[c] += 1
print(d)

    


