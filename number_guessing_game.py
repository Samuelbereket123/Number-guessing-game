import random

def number_guessing_game():


    secret_number = random.randint(1,100)
    attempts = 0
    max_attempts = 10

    print("Welcome to number guessing game!")
    print("I'm thinking of a number in between 1 and 100")
    print(f"You've {max_attempts} attempts to guess it, If I were you I would use it very wisely.")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
             print("Please enter a number which is in the range of 1-1000!")
             continue 

            if guess < secret_number:
                print("Too low try higher")
            elif guess > secret_number:
                print("Too high try lower")
            else:
                print(F"Congratulations you've guessed the number {secret_number} in {attempts} attempts ")
                break

        except ValueError:
            print("This is not a valid input, Please enter an integer")

    if attempts == max_attempts:
        print("You have used all you free attempts sorry not sorry :( ")
   
number_guessing_game()