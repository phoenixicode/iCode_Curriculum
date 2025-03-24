# Import the random module to simulate dice rolls
import random

# Define the snakes and ladders using dictionaries
# Keys represent the starting point and values represent the destination point after encountering a snake or ladder
snake = {16: 6,47: 26,49: 11,56: 53,62: 19,64: 60,87: 24,93: 73,95: 75,98: 78}

ladder = {1: 38,4: 14,9: 31,21: 42,28: 84,36: 44,51: 67,71: 91}
position=0
#while the position reaches 100 keep on throwing dice
while position<=100:
    input('Press Enter')
    # throwing dice
    dice=random.randint(1,6)
    # adding dice to the position
    position+=dice

    # reduce the position if gets more than 100 till the dice is thrown to reach 100
    if position>100:
        position-=dice

    if position==100:
        print('You WOn')
        break
    
    print('Dice:', dice, 'Position:', position)
    if position in snake:
        position=snake[position]
        print('You bitten by snake', position)

    if position in ladder:
        position=ladder[position]
        print('You climbed the ladder', position)
