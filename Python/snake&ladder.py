# Import the random module to simulate dice rolls
import random

# Define the snakes and ladders using dictionaries
# Keys represent the starting point and values represent the destination point after encountering a snake or ladder
snake = {
    16: 6,
    47: 26,
    49: 11,
    56: 53,
    62: 19,
    64: 60,
    87: 24,
    93: 73,
    95: 75,
    98: 78
}

ladder = {
    1: 38,
    4: 14,
    9: 31,
    21: 42,
    28: 84,
    36: 44,
    51: 67,
    71: 91
}

# Initialize player positions
i, j = 0, 0

# Define the dice function to simulate a dice roll (returns a number between 1 and 6)
def dice():
    global d
    d = random.randint(1, 6)  # Randomly generate a number between 1 and 6
    return d

# Main game loop: continue playing until a player reaches position 100
while(i != 100 and j != 100):  # Loop until one of the players wins (reaches position 100)

    # Player 1's turn
    print("Player 1's turn")
    input("Press any key to roll the dice")  # Wait for player input to simulate rolling the dice

    dice()  # Roll the dice for player 1

    # If the player exceeds 100, they move back by the dice roll
    if i > 100:
        i = i - d
    # If the player is less than 100, move forward by the dice roll
    elif i < 100:
        i = i + d
    # If the player reaches exactly 100, they win
    elif i == 100:
        print("Player 1 wins!")
        break  # Exit the loop when player 1 wins

    # Print the current position of player 1
    print("Player 1 is at", i)

    # Check if player 1 encountered a snake
    if i in snake:
        print("Snake encountered!")
        i = snake[i]  # Move the player to the new position after encountering a snake

    # Check if player 1 encountered a ladder
    if i in ladder:
        print("Ladder encountered!")
        i = ladder[i]  # Move the player to the new position after climbing the ladder

    # Print the new position after encountering a snake or ladder
    print("Player 1 is at", i)

    # Player 2's turn
    print("Player 2's turn")
    input("Press any key to roll the dice")  # Wait for player input to simulate rolling the dice

    dice()  # Roll the dice for player 2
    print("Dice rolled:", d)  # Print the result of the dice roll

    # If the player exceeds 100, they move back by the dice roll
    if j > 100:
        j = j - d
    # If the player is less than 100, move forward by the dice roll
    elif j < 100:
        j = j + d
    # If the player reaches exactly 100, they win
    elif j == 100:
        print("Player 2 wins!")
        break  # Exit the loop when player 2 wins

    # Print the current position of player 2
    print("Player 2 is at", j)

    # Check if player 2 encountered a snake
    if j in snake:
        print("Snake encountered!")
        j = snake[j]  # Move the player to the new position after encountering a snake

    # Check if player 2 encountered a ladder
    if j in ladder:
        print("Ladder encountered!")
        j = ladder[j]  # Move the player to the new position after climbing the ladder

    # Print the new position after encountering a snake or ladder
    print("Player 2 is at", j)

# End of the game when one of the players wins (reaches position 100)