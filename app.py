# write a game that have a rock, paper, scissors game  where the user can play against the terminal and choose between rock, paper, scissors the rules are as follows: Rock beats scissors, scissors beats paper, paper beats rock. The game should ask the user for their choice and then the computer should choose a random value and then the winner should be displayed. The game should keep going until the user chooses to quit.

import random

wins = 0
losses = 0
ties = 0

def main():
    global wins, losses, ties
    print("Welcome to Rock, Paper, Scissors!")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Quit")
    user_choice = int(input("Please choose an option: "))
    computer_choice = random.randint(1, 3)

    if user_choice == 1:
        if computer_choice == 1:
            print("You chose Rock and the computer chose Rock. It's a tie!")
            ties   += 1
            play_again()
        elif computer_choice == 2:
            print("You chose Rock and the computer chose Paper. You lose!")
            losses += 1
            play_again()
        else:
            print("You chose Rock and the computer chose Scissors. You win!")
            wins   += 1
            play_again()
    elif user_choice == 2:
        if computer_choice == 1:
            print("You chose Paper and the computer chose Rock. You win!")
            wins   += 1
            play_again()
        elif computer_choice == 2:
            print("You chose Paper and the computer chose Paper. It's a tie!")
            ties   += 1
            play_again()
        else:
            print("You chose Paper and the computer chose Scissors. You lose!")
            losses += 1
            play_again()
    elif user_choice == 3:
        if computer_choice == 1:
            print("You chose Scissors and the computer chose Rock. You lose!")
            losses += 1
            play_again()
        elif computer_choice == 2:
            print("You chose Scissors and the computer chose Paper. You win!")
            wins   += 1
            play_again()
        else:
            print("You chose Scissors and the computer chose Scissors. It's a tie!")
            ties   += 1
            play_again()
    elif user_choice == 4:
        print("Goodbye!")
    else:
        print("Invalid input. Please try again.")
        main()

def play_again():
    global wins, losses, ties
    play_again = input("Would you like to play again? (y/n): ")
    if play_again == "y":
        main()
    elif play_again == "n":
        stats()
        print("Goodbye!")
    else:
        print("Invalid input. Please try again.")
        play_again()

def stats():
    global wins, losses, ties
    print("Your score is: " + str(wins))
    print("The computer's score is: " + str(losses))
    print("There were " + str(ties) + " ties.")

def play():
    main()
    play_again()

play()
