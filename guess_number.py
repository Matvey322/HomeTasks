import random


def guess_the_number():
    secret_number = random.randint(1, 10)
    attempts = 3

    print("I guessed a number from 1 to 10. Try to guess!")

    while attempts > 0:
        guess = int(input("Enter number: "))

        if guess == secret_number:
            print("You guessed the number!")
            return
        elif guess > secret_number:
            print("Less!")
        else:
            print("More!")

        attempts -= 1
        if attempts:
            print(f"Remaining attempts: {attempts}")
        else:
            print(f"You lost! The number you guessed was {secret_number}.")


if __name__ == "__main__":
    guess_the_number()