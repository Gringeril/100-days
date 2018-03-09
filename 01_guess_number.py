import random

print("*** Guess the number from 1 to 100! *** \n")

number = random.randint(1,100)
tries = 1

while True:
    guess = input("Give me a number between 1 and 100: ")
    i=int(guess)

    if i == number:
        print("Congratulations! The number was %s. You guessed it after %s tries :)" % (guess, tries))
        break
    elif i > number:
        print("Try lower!")
        tries = tries + 1
    elif i < number:
        print("Try higher!")
        tries = tries + 1
    else:
        break

