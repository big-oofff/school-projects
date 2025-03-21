age = int(input("How old are you? "))
agediff = str(abs(34 - age))
if age > 34:
    print("You are " + agediff + " years older than Taylor!")
elif age == 34:
    print("You are the same age as Taylor!")
else:
    print("You are " + agediff + " years younger than Taylor!")
