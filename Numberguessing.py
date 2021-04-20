import random
attempts_list = []  #no of attempts list
def show_score():
    if len(attempts_list) <= 0:     #if loop with length of attenpts list condition
        print("there is no high score")
    else:
        print("The current high score is {} attempts".format(min(attempts_list)))
def start_game():
    random_number = int(random.randint(1,10))
    print("hello gamer! Welcome to a game of guesses!")
    player_name = input("What is your name")
    wanna_play = input("hi, {}, wanna play? (Enter yes/no)".format(player_name))
    attempts = 0
    show_score()
    while wanna_play.lower() == "yes":
        try:
            guess = input("Pick a number between 1 and 10")
            if int(guess) < 1 or int(guess) > 10:
                raise ValueError("Please guess a number within the range")
            if int(guess) == random_number:
                print("Nice! you got it")
                attempts += 1
                attempts_list.append(attempts)
                print("it took you {} attempts".format(attempts))
                play_again = input("wanna play again?(Enter Yes/No)")
                attempts = 0
                show_score()
                random_number = int(random.randint(1,10))
                if play_again.lower() == "no":
                    print("thats cool have a good one")
                    break
            elif int(guess) > random_number:
                print("its lower")
                attempts += 1
            elif  int(guess) < random_number:
                print("its higher")
                attempts += 1
        except ValueError as err:
            print(" this is not a valid value. try again!")
            print("({})".format(err))
    else:
        print("okay")
start_game()