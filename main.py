# this is my first python programme
# cards values for each players
playerOne = [11, 3, 5, 8, 2, 9]
playerTwo = [9, 4, 5, 18, 23, 9]

# now we create the scores for each players
playerOneScore = 0
playerTwoScore = 0

# Play seven rounds
for playerOne, playerTwo in zip(playerOne,playerTwo):
    if playerOne > playerTwo:
        print(f"Player One wins with {playerOne} against {playerTwo}")
        playerOneScore = playerOneScore + 1
    elif playerTwo > playerOne:
        print(f"Player two wins with{playerTwo} against {playerOne}")
        playerTwoScore = playerTwoScore + 1
    else:
        print(f"It is a draw with {playerOne}")

# Determine who won the game
if playerOneScore > playerTwoScore:
    print("Player one wins the game!")
elif playerTwoScore > playerOneScore:
    print("Player two wins the game ")
else:
    print("The Game is a tie")

