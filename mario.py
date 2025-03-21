while True:
    try:
        height = int(input("Enter staircase height between 0 and 23 inclusive: "))
        if 0 <= height <= 23:
            for i in range(1, height + 1):
                print(" " * (height - i) + "#" * i + " " * 3 + "#" * i)
            break  
        else:
            print("Invalid input")
    except:
        print("Invalid input. Enter an integer between 0 and 23 inclusive:")

