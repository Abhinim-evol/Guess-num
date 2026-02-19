import random

correctAnswer = random.randint(1, 100)
gameOver = False

while gameOver == False:
    playerGuess = int(input("Guess a number between 1 and 100: "))

    if playerGuess == correctAnswer:
        print("Correct! You Win!")
        gameOver = True

    elif playerGuess > correctAnswer:
        print("Too High! Guess Again!")

    else:
        print("Too Low! Guess Again!")
