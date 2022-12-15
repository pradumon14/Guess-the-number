# Import the necessary modules
import random

# Define some game constants
MAX_GUESSES = 5
MAX_NUMBER = 10

# Print an introduction to the game
print("Welcome to the guess the number game!")
print("I'm thinking of a number between 1 and %d. You have %d guesses to guess what it is." % (MAX_NUMBER, MAX_GUESSES))

# Generate a random number for the player to guess
number = random.randint(1, MAX_NUMBER)

# Keep track of the number of guesses the player has made
num_guesses = 0

# Start a loop to let the player guess until they either guess the number or run out of guesses
while num_guesses < MAX_GUESSES:
  # Get the player's guess
  guess = int(input("What's your guess? "))
  
  # Check if the guess is correct
  if guess == number:
    # If the guess is correct, print a message and end the game
    print("You got it! The number was %d" % number)
    break
  else:
    # If the guess is not correct, print a message and subtract one from the number of guesses remaining
    print("Sorry, that's not it.")
    num_guesses += 1

# If the player ran out of guesses, print a message telling them they lost
if num_guesses == MAX_GUESSES:
  print("Sorry, you ran out of guesses. The number was %d" % number)
