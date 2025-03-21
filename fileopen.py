import time
all = set()
fhand = open("mbox-short.txt")
for line in fhand:
    if line.startswith("From: "):
        all.add(line[6:].strip())
for email in all:
    print(email)

        
