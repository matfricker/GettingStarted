import random

secret_num = random.randint(1,10)

GUESS = 0
COUNT = 0
LIMIT = 10
REMAINING_GUESSES = 0
OUT_OF_GUESSES = False

def check_num():
    if GUESS > secret_num:
        print("Too high, " + str(REMAINING_GUESSES) + " left")
    elif GUESS < secret_num:
        print("Too low, " + str(REMAINING_GUESSES) + " left")

print("Pick a number between 1 and 10.")
print("You have " + str(LIMIT) + " gueses.")

while GUESS != secret_num and not OUT_OF_GUESSES:
    if COUNT < LIMIT:
        GUESS = int(input("Enter your guess:\n"))
        COUNT += 1
        REMAINING_GUESSES = LIMIT - COUNT
        check_num()
    else:
        OUT_OF_GUESSES = True

if OUT_OF_GUESSES:
    print("No more guesses, YOU LOSE!")
else:
    print("You Win!")
