"""
You have to build a "Number Guessing Game," in which a winning number is set to some integer value. The Program should take input from the user, and if the entered number is less than the winning number, a message should display that the number is smaller and vice versa.

Instructions:
1. You are free to use anything we've studied till now.
2. The number of guesses should be limited, i.e (5 or 9).
3. Print the number of guesses left.
4. Print the number of guesses he took to win the game.
5. “Game Over” message should display if the number of guesses becomes equal to 0.
You are advised to participate in solving this problem. This task helps you to become a good problem solver and helps you accepting the challenge and acquiring new skills.
#Solution:
"""
import random
Actual_Number = random.randint(1,30)     #Generate a random number between 1 to 30
#print(Actual_Number)    #see the actual number (For Tasting)

print("Welcome to the" "\"" "Number Guessing Game,,,," "\"")  #Escape Sequences "\""
print("\nGame Levels:")
print(" Easy\n Medium\n Hard\n")
choose= input("Choose your Level: ")

# EASY Level Code
if choose.capitalize() == "Easy":
    No_Guess = 1
    while(True):
        Player_Guess = int(input("Enter your Guess Number: "))

        if Player_Guess >= 0:
            if Player_Guess == Actual_Number:
                print("Congratulations!!!\n You are WIN....")
                print("You win this game using ", (No_Guess), "times guess")
                break
            else:
                if Player_Guess > Actual_Number:
                    print("Your guess is not right yet.\n", "The Actual number will be less then ", Player_Guess,
                          "\nPlease guess again,,,,")
                    print("Note: You're ", (9 - No_Guess), "times guess remain.")
                else:
                    print("Your guess is not right yet.\n", "The Actual number will be gater then ", Player_Guess,
                          "\nPlease guess again,,,,")
                    print("Note: You're ", (9 - No_Guess), "times guess remain.")
        if (9 - No_Guess) == 0:
            print("Your have 0 guess remain\n","Game Over.....!")
            break
        No_Guess = No_Guess + 1

#Medium Level Code
elif choose.capitalize() == "Medium":
    No_Guess = 1
    while(True):
        Player_Guess = int(input("Enter your Guess Number: "))

        if Player_Guess >= 0:
            if Player_Guess == Actual_Number:
                print("Congratulations!!!\n You are WIN....")
                print("You win this game using ", (No_Guess), "times guess")
                break
            else:
                if Player_Guess > Actual_Number:
                    print("Your guess is not right yet.\n", "The Actual number will be less then ", Player_Guess,
                          "\nPlease guess again,,,,")
                    print("Note: You're ", (7 - No_Guess), "times guess remain.")
                else:
                    print("Your guess is not right yet.\n", "The Actual number will be gater then ", Player_Guess,
                          "\nPlease guess again,,,,")
                    print("Note: You're ", (7 - No_Guess), "times guess remain.")
        if (7 - No_Guess) == 0:
            print("Your have 0 guess remain\n","Game Over.....!")
            break
        No_Guess = No_Guess + 1

#Hard Level Code
elif choose.capitalize() == "Hard":
    No_Guess = 1
    while(True):
        Player_Guess = int(input("Enter your Guess Number: "))

        if Player_Guess >= 0:
            if Player_Guess == Actual_Number:
                print("Congratulations!!!\n You are WIN....")
                print("You win this game using ", (No_Guess), "times guess")
                break
            else:
                if Player_Guess > Actual_Number:
                    print("Your guess is not right yet.\n", "The Actual number will be less then ", Player_Guess,
                          "\nPlease guess again,,,,")
                    print("Note: You're ", (5 - No_Guess), "times guess remain.")
                else:
                    print("Your guess is not right yet.\n", "The Actual number will be gater then ", Player_Guess,
                          "\nPlease guess again,,,,")
                    print("Note: You're ", (5 - No_Guess), "times guess remain.")
        if (5 - No_Guess) == 0:
            print("Your have 0 guess remain\n","Game Over.....!")
            break
        No_Guess = No_Guess + 1

else:
    print("Wrong input.\n You may input the wrong level. Please check your input level again.")