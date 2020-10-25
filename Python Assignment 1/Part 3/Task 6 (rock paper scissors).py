options = ["rock", "paper", "scissors"]

game = True

while game:
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    # Player 1 validation
    valid = False
    while not valid:
        player1 = int(input("Player 1. Choose a number: "))
        if (player1 >= 1 and player1 <= 3):
            valid = True
        else:
            print("Invalid Choice.")
            valid = False
    # Player 2 validation
    valid = False
    while not valid:
        player2 = int(input("Player 2. Choose a number: "))
        if (player2 >= 1 and player2 <= 3):
            valid = True
        else:
            print("Invalid Choice.")
            valid = False

    if player1 == player2:
        print("Tie")
    elif (player1 == 1 and player2 == 3) or (player1 == 2 and player2 == 1) or (player1 == 3 and player2 == 2):
        print("Congratulations to Player 1")
    else:
        print("Congratulations to Player 2")

    repeat = input("Do you want to Play again?(Y/N): ")

    repeat = repeat[0].lower()
    if (repeat == 'y'):
        game = True
    else:
        game = False