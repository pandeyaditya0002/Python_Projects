import random

# This program is a simple number guessing game.


# Get the upper limit for the random number range from the user
top_of_range = input("Type a number: ")

# Check if the input is a digit
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    # Ensure the number is greater than 0
    if top_of_range <= 0:
        print('Please type a number larger than 0 next time.')
        quit()
else:
    print('Please type a number next time.')
    quit()

# Generate a random number between 0 and the upper limit
random_number = random.randint(0, top_of_range)
guesses = 0

# Start the guessing loop
while True:
    guesses += 1
    user_guess = input("Make a guess: ")

    # Check if the guess is a digit
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time.')
        continue
    
    #check if the guess is correct
    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")

# Print the number of guesses it took to get the correct answer
print("You got it in", guesses, "guesses")