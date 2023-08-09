import random

def gameWin(computer, you):
    if computer == you:
        return None
    elif computer == "r":
        if you == "s":
            return False
        elif you == "p":
            return True
    elif computer == "p":
        if you == "r":
            return False
        elif you == "s":
            return True
    elif computer == "s":
        if you == "p":
            return False
        elif you == "r":
            return True
        
print("Computer has selected from: Rock(r), Paper(p), Scissor(s)?")
randNo = random.randint(1,3) 

if randNo == 1:
    computer = "r"
elif randNo == 2:
    computer = "p"
elif randNo == 3:
    computer = "s"

you = input("Your Turn: Rock(r), Paper(p), Scissor(s)?")
a = gameWin(computer, you)

print(f"Computer chose {computer}")
print(f"You chose {you}")

if a == None:
    print("The game was a tie!")
elif a:
    print("You won!")
else:
    print("You lost!")