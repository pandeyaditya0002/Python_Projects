
# This program is a simple computer quiz game.


# Display a welcome message
print("Welcome to my computer quiz!")

# Ask the user if they want to play
playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

# Question 1
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1  # Increase score if correct
else:
    print("Incorrect!")

# Question 2
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

# Question 3
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

# Question 4
answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

# Display final score and percentage
print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")
