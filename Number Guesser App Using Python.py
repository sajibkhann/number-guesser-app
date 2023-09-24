import random

def guess_number():
    while True:
        correct_answer = random.randint(1, 50)
        attempts = 0
        max_attempts = 5 
        print("-----------------------------------------------------------------")
        print("Welcome to the Number Guessing Game!")
        print("Guess a number from 1 to 50. You have five attempts")

        while attempts < max_attempts:
            try:
                guess = int(input("Enter your guess: "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            attempts += 1

            if guess < correct_answer:
                print("Correct answer is greater!")
            elif guess > correct_answer:
                print("Correct answer is smaller!")
            else:
                print(f"Congratulations! You guessed the number {correct_answer} in {attempts} attempts.")
                break
        else:
            print(f"Sorry, you've reached the maximum number of attempts. The correct number was {correct_answer}.")

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break

guess_number()
