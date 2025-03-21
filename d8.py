def oddoreven(int): return True if int % 2 == 0 else False
num = int(input("Enter integer: "))
print(f"{num} is even" if oddoreven(num) == True else f"{num} is odd")

