# Initialize the game board as a list of 10 spaces (index 0 is not used).
board = [' ' for x in range(10)]


# Function to insert a letter (X or O) into a position on the board.
def insert_letter(letter, pos):
    board[pos] = letter


# Function to check if a space on the board is empty.
def SpaceIsFree(pos):
    return board[pos] == ' '


# Function to print the game board with positions.
def printBoard(board):
    # Print the game board using a list of spaces and positions.
    print('   |   |   ')
    print(f" {board[1]} | {board[2]} | {board[3]} ")
    print("   |   |   ")
    print("-----------")
    print('   |   |   ')
    print(f" {board[4]} | {board[5]} | {board[6]} ")
    print("   |   |   ")
    print("-----------")
    print('   |   |   ')
    print(f" {board[7]} | {board[8]} | {board[9]} ")
    print("   |   |   ")


# Function to check if the game board is full (a tie).
def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


# Function to check if a player has won (based on the letter "X" or "O").
def IsWinner(board, letter):
    # Check for all possible winning combinations.
    f1 = (board[1] == letter and board[2] == letter and board[3] == letter)
    f2 = (board[4] == letter and board[5] == letter and board[6] == letter)
    f3 = (board[7] == letter and board[8] == letter and board[9] == letter)
    f4 = (board[1] == letter and board[4] == letter and board[7] == letter)
    f5 = (board[2] == letter and board[5] == letter and board[8] == letter)
    f6 = (board[3] == letter and board[6] == letter and board[9] == letter)
    f7 = (board[1] == letter and board[5] == letter and board[9] == letter)
    f8 = (board[3] == letter and board[5] == letter and board[7] == letter)

    # Check if any of the winning combinations are met.
    f = f1 or f2 or f3 or f4 or f5 or f6 or f7 or f8
    return f


# Function for the human player to make a move.
def playerMove():
    run = True
    while run:
        move = input("Please select a position to enter the X between 1 to 9")
        try:
            move = int(move)
            if 1 <= move <= 9:
                if SpaceIsFree(move):
                    run = False
                    insert_letter('X', move)
                else:
                    print("Sorry, this space is occupied.")
            else:
                print("Please type a number between 1 and 9.")
        except:
            print("Please type a number.")


# Function for the computer player to make a move.
def computerMove():
    # Create a list of possible moves (positions with a space) on the board.
    possibleMoves = [x for x, letter in enumerate(board) if letter == " " and x != 0]
    move = 0

    # Check if the computer can win in the next move.
    for let in ['O', 'X']:
        for i in possibleMoves:
            boardcopy = board[:]
            boardcopy[i] = let
            if IsWinner(boardcopy, let):
                move = i
                return move

    # Check if any of the corners are open.
    corneropen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            corneropen.append(i)

    if len(corneropen) > 0:
        move = selectRandom(corneropen)
        return corneropen[move]

    # Place "O" in the center if it's available.
    if 5 in possibleMoves:
        move = 5
        return move

    # Check if any of the edges are open.
    edgesopen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesopen.append(i)

    if len(edgesopen) > 0:
        move = selectRandom(edgesopen)
        return edgesopen[move]
    return move


# Function to select a random move.
def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return r


# Main game loop
def main():
    print("Welcome to the game!")
    printBoard(board)

    while not isBoardFull(board):
        if not IsWinner(board, 'O'):
            playerMove()
            printBoard(board)
        else:
            print("Sorry, you lose!")
            break
        if not IsWinner(board, 'X'):
            comp_move = computerMove()
            if comp_move == 0:
                print(" ")
            else:
                insert_letter('O', comp_move)
                print(f'Computer placed an O on position {comp_move}:')
                printBoard(board)
        else:
            print("YOU WIN!")
            break

    if isBoardFull(board):
        print("Tie Game")

# Start the game and allow replay.
while True:
    x = input("Do you want to play again? (y/n) ")
    if x.lower() == 'y':
        board = [' ' for x in range(10)]
        print('--------------------------')
        main()
    else:
        break