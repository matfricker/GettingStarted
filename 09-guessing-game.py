import random

secret_num = random.randint(1,10)

guess = 0
count = 0
limit = 10
remaining_guesses = 0
out_of_guesses = False

def checkNum():
    if guess > secret_num:
        print("Too high, " + str(remaining_guesses) + " left")
    elif guess < secret_num:
        print("Too low, " + str(remaining_guesses) + " left")

print("Pick a number between 1 and 10.")
print("You have " + str(limit) + " gueses.")

while guess != secret_num and not(out_of_guesses):
    if count < limit:
        guess = int(input("Enter your guess:\n"))
        count += 1
        remaining_guesses = limit - count
        checkNum()
    else:
        out_of_guesses = True

if out_of_guesses:
    print("No more guesses, YOU LOSE!")
else:
    print("You Win!")
