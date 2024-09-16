import random

secret_number = random.randint(1, 15)
while True:
    guess = int(input("\nI'm thinking of a number between 1 and 15. Can you guess it?"))

    match guess:
          case _ if guess == secret_number:
                print("Congratulations, you guessed it!")
                break  # Exit the loop if the guess is correct
          case _ if guess > secret_number:
                print("Oops, your guess is a bit high. Try again!")
          case _ if guess < secret_number:
                print("Nope, your guess is a bit low. Give it another shot!")

play_again = input("Do you want to play again? yes/no: ").lower()

if play_again == 'yes':
      secret_number = random.randint(1, 15)

else:
      print("Thanks for playing!")