def nextTurn(count,board):
    if count%2 == 0:
        x, y = input("It is o's turn (row column): ").split(" ")
        board[int(x) - 1][int(y) - 1] = "o"
    elif count%2 == 1:
        x, y = input("It is x's turn (row column): ").split(" ")
        board[int(x) - 1][int(y) - 1] = "x"
    count += 1
    printBoard(board)
    return count, board

def printBoard(a):
    print(a[0][0] + "|" + a[0][1] + "|" + a[0][2])
    print("-+-+-")
    print(a[1][0] + "|" + a[1][1] + "|" + a[1][2])
    print("-+-+-")
    print(a[2][0] + "|" + a[2][1] + "|" + a[2][2])

def checkWin(board, state):
    for i in range(3):  # Checks the rows
        if board[i][0] == board[i][1] and board[i][0] == board[i][2] and board[i][0] != " ":
            state = True

    for i in range(3):  # Checks the columns
        if board[0][i] == board[1][i] and board[0][i] == board[2][i] and board[0][i] != " ":
            state = True
    
    if board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] != " ":    # checks diagonal
        state = True
    
    if board[2][0] == board[1][1] and board[2][0] == board[0][2] and board[2][0] != " ":    # checks diagonal
        state = True
    
    # if any conditions are met then state is set to True, state indicates if a game is won or not
    
    return state

def gameFlow():
    num = 0
    state = False
    grid = [[" "," "," "],[" "," "," "],[" "," "," "]]

    while state == False and num < 10:
        num, grid = nextTurn(num, grid)
        state = checkWin(grid, state)
    
    if state == True:
        if num%2 == 1:
            print("o wins")
        elif num%2 == 0:
            print("x wins")
        quit()

    print("nobody wins")
    
gameFlow()

