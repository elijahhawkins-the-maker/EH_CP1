#EH 1st fix the game!

import random
def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
   
    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    #logic error: the total attempts equal to 11 and not 10
    attempts = 1
    
    game_over = False
    while not game_over:
   
    #runtime error: the input was not defined as an integer
        guess = int(input("Enter your guess: "))
       
        if attempts >= max_attempts:
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
            game_over = True
      
        if guess == number_to_guess:
            print("Congratulations! You've guessed the number!")
            game_over = True
     
        elif guess > number_to_guess:
            print("Too high! Try again.")
       
        elif guess < number_to_guess:
            print("Too low! Try again.")  

        attempts += 1
        # logic error: there is no need for a continue function
    print("Game Over. Thanks for playing!")
start_game()