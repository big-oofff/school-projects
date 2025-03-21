while True:
    change = input("O hai! How much change is owed? (Type 'break' to exit): ")
    if change.lower() == 'break':
        break  
    
    try:
        change = float(change) * 100
        if change < 0:
            print("Please enter a positive value.")
        else:
            change = round(change)
    except ValueError:
        print("Please enter a valid numerical value.")
        continue 

    coin_count = 0
    while change > 0:
        if change == 25 or change == 10 or change == 5 or change == 1:
            coin_count += 1
            break
        elif change > 25:
            coin_count += change // 25
            change = change % 25
        elif change > 10:
            coin_count += change // 10
            change = change % 10
        elif change > 5:
            coin_count += change // 5
            change = change % 5
        else:
            coin_count += change // 1
            change = change % 1
    print(f"Total coins needed: {coin_count}")
