'''The Hand Cricket game is a simple interactive batting–bowling simulation between the user and the computer.
The game begins with the user batting first, while the computer bowls. In each turn, the computer randomly selects a number between 1 and 10, and the user also enters a number within the same range.
If the two numbers do not match, the user’s entered number is added to their total score, representing runs scored.
This continues until the user’s number matches the computer’s number, which means the user is “out” and their batting innings ends.
Once the user is out, the game switches roles: now the computer bats and the user bowls.
In computer batting, the computer continues to generate random numbers between 1 and 10, while the user inputs a number to bowl.
If the two numbers are different, the computer’s randomly generated number is added to the computer’s total score. However, if both numbers match, the computer is declared “out,” ending its innings as well.
After both innings are completed, the final scores of the user and the computer are compared. If the user’s score is higher, the user wins. If the computer’s score is higher, the user loses.
If both scores are equal, the match is considered a tie. The game is entirely based on number matching, user input, and randomness from the computer, making it easy to play while still being engaging and unpredictable.'''
import random
print("Welcome to Hand cricket game")
sum_of_user=0
sum_of_computer=0

game=1
while game==1:
    choice_of_computer = random.randint(1, 10)
    user_input = int(input("enter your choice"))
    if user_input>10 or user_input<0:
        print("Invalid input\nTry again")
        continue

    print(f"Your choice is {user_input}")
    print(f"Computer choice is {choice_of_computer}")

    if(user_input!=choice_of_computer):
        sum_of_user+=user_input
        print(f"Your current score is {sum_of_user}")
    else:
        print("User out")
        print("Its computer turn")
        while game == 1:
            choice_of_computer = random.randint(1, 10)
            user_input = int(input("enter your choice"))
            print(f"Your choice is {user_input}")
            print(f"Computer choice is {choice_of_computer}")
            if (user_input != choice_of_computer):
                sum_of_computer += choice_of_computer
                print(f"Computer current score is {sum_of_computer}")
            else:
                print("Computer out")
                game=0


print(f"Your final score is {sum_of_user}")



print(f"Computer final score is {sum_of_computer}")

if sum_of_user>sum_of_computer:
    print("Congrajulations you won the game")
elif(sum_of_computer>sum_of_user) :
    print("Sorry you lost the game ")
else :
    print('Its a tie')


