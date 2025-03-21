import random
print("*************************")
print("*WELCOME TO TIC TAC TOE!*")
print("*************************")




def display_board(board):
    print(f"""
     {board[0]} | {board[1]} | {board[2]} 
    -----------
     {board[3]} | {board[4]} | {board[5]} 
    -----------
     {board[6]} | {board[7]} | {board[8]} 
    """)

def is_winner(board, marker):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]              
    ]
    return any(all(board[pos] == marker for pos in condition) for condition in win_conditions)

def is_full(board):
    return all(str(cell).isdigit() == False for cell in board)

def player_move(board, current_player):
    while True:
        try:
            move = int(input(f"Player {current_player}, choose a position (1-9): ")) - 1
            if board[move].isdigit():
                board[move] = current_player
                break
            else:
                print("Position already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please choose a number between 1 and 9.")

def computer_move(board, smart):
    available_moves = [i for i, cell in enumerate(board) if cell.isdigit()]
    if not smart:
        return random.choice(available_moves)

    def minimax(board, depth, is_maximizing):
        if is_winner(board, "O"):
            return 10 - depth
        if is_winner(board, "X"):
            return depth - 10
        if is_full(board):
            return 0
        
        available_moves = [i for i, cell in enumerate(board) if cell.isdigit()]
       
        if is_maximizing:
            best_score = float('-inf')
            for move in available_moves:
                board[move] = "O"
                score = minimax(board, depth + 1, False)
                board[move] = str(move + 1)
                best_score = max(score, best_score)
            return best_score
        else: 
            best_score = float('inf')
            for move in available_moves:
                board[move] = "X"
                score = minimax(board, depth + 1, True)
                board[move] = str(move + 1)
                best_score = min(score, best_score)
            return best_score

    best_move = None
    best_score = float('-inf')
    for move in available_moves:
        board[move] = "O"
        score = minimax(board, 0, False)
        board[move] = str(move + 1)
        if score > best_score:
            best_score = score
            best_move = move

    return best_move

def two_player_mode(board):
    player_turn = True
    display_board(board)
    while True:
        current_player = "X" if player_turn else "O"
        player_move(board, current_player)
        display_board(board)
        if is_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break
        if is_full(board):
            print("It's a tie!")
            break
        player_turn = not player_turn

def one_player_mode(board, smart):
    player_turn = True
    display_board(board)
    while True:
        if player_turn:
            player_move(board, "X")
        else:
            print("Computer's turn...")
            move = computer_move(board, smart)
            print(f"Computer picked {move + 1}")
            board[move] = "O"
        display_board(board)
        if is_winner(board, "X"):
            print("Player wins!")
            break
        if is_winner(board, "O"):
            print("Computer wins!")
            break
        if is_full(board):
            print("It's a tie!")
            break
        player_turn = not player_turn

def zero_player_mode(board, smart, num_of_games):
    x_count, o_count, tie_count = 0, 0, 0
    for i in range(num_of_games):
        display_board(board)
        while True:
            print("Computer's turn...")
            move = computer_move(board, smart)
            print(f"Computer picked {move + 1}")
            board[move] = "X" if board.count("X") <= board.count("O") else "O"
            display_board(board)
            if is_winner(board, "X"):
                x_count += 1
            if is_winner(board, "O"):
                o_count += 1
            if is_winner(board, "X") or is_winner(board, "O"):
                print("Game over!")
                break
            if is_full(board):
                print("It's a tie!")
                tie_count += 1
                break
        board = [str(i) for i in range(1, 10)]
    print(f"Computer X won {x_count} times, Computer O won {o_count} times, they tied {tie_count} times.")

def tic_tac_toe():
    board = [str(i) for i in range(1, 10)]
    mode = input("Choose mode: 0 (Zero Player), 1 (One Player), 2 (Two Player): ")

    while mode not in ["0", "1", "2"]:
        mode = input("Invalid choice. Please choose 0, 1, or 2: ")

    if mode in ["0", "1"]:
        smart_mode = input("Do you want the computer to play smart? (y/n): ").lower()
        smart = smart_mode == "y"

    if mode == "2":
        two_player_mode(board)
    elif mode == "1":
        one_player_mode(board, smart)
    elif mode == "0":
        num = int(input("Enter number of games to be simulated:  "))
        zero_player_mode(board, smart, num_of_games=num) 
tic_tac_toe()