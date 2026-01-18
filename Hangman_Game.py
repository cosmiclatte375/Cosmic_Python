import random
import Hang_man_stages as A
words=["apple","cosmic","galaxy","nova","lattee","coffee"]
lives=6
choosen=random.choice(words)
print(choosen)
length=len(choosen)
display=[]
for i in range(length):
    display.append("_")
print(display)
game_over=False
while not game_over:
    guess=input("Enter your guess: ").lower()
    for i in range (length):
        letter=choosen[i]
        if letter==guess:
            display[i]=guess
    print(display)
    if guess not in choosen:
        print("Your guess is not in the word")
        lives-=1
        print(f"You have {lives} lives left")
        print(A.stages[lives])
        if lives==0:
            game_over=True
            print("You lose!")

    if "_" not in display:
        game_over=True
        print("You win!")