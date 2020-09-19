from random import randint
ocean = []
for x in range(0, 5):
    ocean.append(["O"] * 5)
existing_ships = []

def print_board(board):
    for row in board:
        print(" ".join(row))

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

def create_unique_ship():
    while 1:
        ship = [random_row(ocean), random_col(ocean)]
        if ship in existing_ships:
            continue
        else:
            return ship


# this function checks if the guess hits or misses.
# it returns: 0 for already guessed, 1 for hit, 2 for miss, 3 for invalid input
def hit_or_miss(guess_row, guess_col):
    ship = [guess_row, guess_col]
    if ocean[guess_row][guess_col] == "x" or ocean[guess_row][guess_col] == "_":
        print("you already guessed this one, try again")
        print_board(ocean)
        return 0;
    elif ship in existing_ships:
        ocean[guess_row][guess_col] = "x"
        print("HIT")
        return 1
    elif guess_row > 4 or guess_col > 4 :
        print("enter a valid number")
        print_board(ocean)
        return 3
    else:
        ocean[guess_row][guess_col] = "_"
        print("MISS")
        print_board(ocean)
        return 2

num_ships = int(input("Number of ships: "))
for turn in range(num_ships):
    existing_ships.append(create_unique_ship())

print(existing_ships)
sunk_ships = 0
for turn in range(5):
    print ("Turn", turn + 1)
    guess_row = int(input("enter row: "))
    guess_col = int(input("enter col: "))
    if hit_or_miss(guess_row, guess_col) == 1:
        sunk_ships = sunk_ships + 1
        print_board(ocean)
        if sunk_ships == len(existing_ships):
            print ("all ships destroyed")
            break

