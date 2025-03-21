def initialize_board(size):
    board = [[(size * size - 1) - (i * size + j) for j in range(size)] for i in range(size)]
    board[size - 1][size - 1] = 0 
    
    if size % 2 == 0:  
        board[size - 1][size - 2], board[size - 1][size - 3] = board[size - 1][size - 3], board[size - 1][size - 2]  # Swap 1 and 2
    return board

def print_board(board):
    for row in board:
        print(" ".join(f"{num:2}" if num != 0 else "  " for num in row))
    print()

def find_empty_space(board):
    for i, row in enumerate(board):
        for j, num in enumerate(row):
            if num == 0:
                return i, j
    return None

def is_solved(board):
    size = len(board)
    expected = [i for i in range(1, size * size)] + [0]
    return sum(board, []) == expected

def move_tile(board, direction):
    size = len(board)
    x, y = find_empty_space(board)
    dx, dy = {"up": (1, 0), "down": (-1, 0), "left": (0, 1), "right": (0, -1)}.get(direction, (0, 0))
    
    new_x, new_y = x + dx, y + dy
    if 0 <= new_x < size and 0 <= new_y < size:
        board[x][y], board[new_x][new_y] = board[new_x][new_y], board[x][y]
        return True
    return False

def main():
    while True:
        try:
            size = int(input("Enter board size (minimum 3, maximum 9): "))
            if size < 3 and size > 9:
                print("Unsuitable size")
                continue
            break
        except ValueError:
            print("Invalid input")
    
    board = initialize_board(size)
    
    while True:
        print_board(board)
        if is_solved(board):
            print("You win")
            return
        
        move = input("Enter move (up, down, left, right, or 'quit' to exit): ").strip().lower()
        if move == "quit":
            print("Game exited")
            return
        if move not in {"up", "down", "left", "right"}:
            print("Invalid move")
            continue
        if not move_tile(board, move):
            print("Invalid move")

if __name__ == "__main__":
    main()
