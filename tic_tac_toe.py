def print_board(board):
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('--|---|--')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('--|---|--')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])


def check_win(board):
    win_conditions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != " ":
            return True
    return False


def check_draw(board):
    return all(x != ' ' for x in board)


def tic_tac_toe():
    board = [' ' for _ in range(9)]
    current_player = 'X'
    
    while True:
        print_board(board)
        
        try:
            position = int(input(f"Player {current_player}, enter position (0-8): "))
            if position < 0 or position > 8:
                print("Invalid position!")
                continue
        except:
            print("Enter a valid number!")
            continue
        
        if board[position] == ' ':
            board[position] = current_player
            
            if check_win(board):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            
            if check_draw(board):
                print_board(board)
                print("It's a draw!")
                break
            
            current_player = 'O' if current_player == 'X' else 'X'
        
        else:
            print("Position already taken. Try again.")


tic_tac_toe()