# ROCK PAPER SCISSOR game

from random import randint


def game(comp,you):
    if comp==you:
        return None

    elif comp=="rock":
        if you=="scissor":
            return False
        elif you=="paper":
            return True
    
    elif comp=="paper":
        if you=="rock":
            return False
        elif you=="scissor":
            return True
    
    elif comp=="scissor":
        if you=="paper":
            return False
        elif you=="rock":
            return True

while True:
    a=randint(1,3)

    if a==1:
        comp="rock"
    elif a==2:
        comp="paper"
    elif a==3:
        comp="scissor"
    
    you=input("Enter rock, paper or scissor: ")

    if you=="exit":
        break
    
    result=game(comp,you)
    print(f"Computer choice : {comp}")
    if result==None:
        print("It's a tie")
    elif result==False:
        print("You loose !!!!")
    elif result==True:
        print("You win !!!!")
    print("*************")
    print("Enter exit to exit the play")
