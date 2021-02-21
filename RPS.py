import random
answer = "Y"

print("Let's play Rock...Paper...Scissors!")


def askUser():
    global userchoice
    userchoice= input("Please input R, P, or S: ")
    return userchoice

def converter(choice):
    if choice == "R":
        choice = "Rock"
    elif choice == "P":
        choice = "Paper"
    else:
        choice = "Scissors"
    return choice

while answer == "Y":

    askUser()

    computerchoice = random.randint(0,2)
    if computerchoice == 0:
        computerchoice = "R"
    elif computerchoice == 1:
        computerchoice = "P"
    else:
        computerchoice == 2
        computerchoice = "S"
    print("Computer says: " + converter(computerchoice))

    if userchoice == computerchoice:
        print("It's a draw!")
    else:
        if userchoice == "R":
            if computerchoice == "S":
                print("You won! Rock smashes Scissors!")
            elif computerchoice == "P":
                print("You lost. Try again!")
        if userchoice == "S":
            if computerchoice == "R":
                print("You lost. Try again!")
            elif computerchoice == "P":
                print("You won! Scissors cut Paper!")
        else:
            if computerchoice == "S":
                print("You lost!")
            elif computerchoice == "R":
                print("You won! Paper wraps Rock!")

    answer = input("Do you want to play again? Y/N")
    answer = answer.upper()






