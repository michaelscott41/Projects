import random
number = random.randint(1, 10)

def start_game():

    current_high_score = 5
    guess_remaining = [1, 2, 3, 4, 5]
    guesses_used = 0
    group = []

    # write your code inside this function.

    input("Welcome to the Number Guessing Game!  Press ENTER to start.")
    name = input("What is  your name, my friend?  ")

    play_again = True

    while play_again == True:
        guesses_used = 0
        number = random.randint(1, 10)

        print ("The current high score is {}  ".format(current_high_score))

        for guesses in guess_remaining:
            try:
                guess = input("{}, I am thinking of a number between 1 and 10.  What do you think it is?  ".format(name.capitalize()))
                guess = int(guess)

            except ValueError:
                print("Hey, it looks like we need a valid number.  Try again!".format(guess))
                continue

            try:
                guesses_used += 1

                if not guess > 0 or not guess < 11:

                    print("Sorry, that isn't a valid number.  Please try a number between 1 and 10.")
                    guesses_used -= 1
                    guess_remaining.append([1])
                    continue

            except ValueError:
                print("That isn't a valid number.  Please select a number between 1 and 10")
                continue
            else:
                if guess > number:
                    print("Ohhh, sorry.  It looks like your guess was too high.  Try again!")

                elif guess < number:
                    print("Shoot, it looks like your number is low.  Try again!")

                elif guess == number:
                    break

        if guess == number:
            print("That is awesome, {}!  You managed to guess my number in {} guesses.  Way to go!".format(name.capitalize(), guesses_used))


        if guess != number:
            print("Sorry {}, I was actually thinking of {}.".format(name.capitalize(), number))

        new_high_score = guesses_used
        if new_high_score < current_high_score:
            current_high_score = new_high_score

        answer = input('Do you want to play again? (yes/no):  ')

        if answer == 'yes'.lower():
            play_again = True

        else:
            print("Thank you so much for playing!  Have a great day.")
            exit()
if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
