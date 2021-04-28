import random
print("Number Guess Game")
number = random.randint(1, 9)
chances = 0
print("Guess a number between 1 , 9")
while chances < 3:
    guess = int(input("ENTER YOUR GUESS:-")) 
    if number == guess:
        print("CONGRATULATIONS!!! YOU WON")
        break
    elif number > guess:
        print("Your number was too Low The number is Higher than", guess)
    else:
        print("Your number was too High The number is Lower than", guess)
    chances += 1 
if not chances < 3:
    print("YOU LOSE!!! The number was", number)