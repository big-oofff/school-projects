def make_board(n):
    """
    n is an integer between 3 and 9.  makes a board which is a list of n lists, each list representing a row in the board.  assigns a value from the (n*n - 1) to 0 to each tile.  if n is even, the 2 and 1 tiles are swapped.
    """
    #board = []
    val = n*n-1
    for i in range(n):
        board.append([])
    for i in range(n):
        for j in range(n):
            board[i].append(val)
            val-=1
    if n % 2 == 0:
        board[n-1][n-3], board[n-1][n-2] = board[n-1][n-2], board[n-1][n-3]
        

def display_board():
    n = len(board)
    for i in range(n):
        for j in range(n):
            num = board[i][j]
            if num == 0: print("  ", end = " ")
            elif num < 10: print(" " + str(num), end = " ")
            else: print(str(num), end = " ")
        print()
            



board = []
num_rows = 4

#num_rows = valid_input()
make_board(num_rows)
display_board()
##
##while True:
##    tile = int(input("Tile: "))
##    blank = find_blank()
##    tile = find_tile(tile)
##    if valid_move(blank[0], blank[1], tile[0], tile[1]):
##        swap_tile(blank[0], blank[1], tile[0], tile[1])
##    else:
##        print("not a valid move")
##    display_board()
##    if check_win():
##        print("Yay!!!")


