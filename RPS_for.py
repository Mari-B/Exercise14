import random
userpoints = 0
computerpoints = 0

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

for i in range (0, 3):

    askUser()

    computerchoice = random.randint(0,1)
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
        userpoints += 1
        computerpoints += 1
        print("Result: User ", userpoints, " Computer ", computerpoints)

    else:
        if userchoice == "R":
            if computerchoice == "S":
                print("You won! Rock smashes Scissors!")
                userpoints += 1
                print("Result: User ", userpoints, " Computer ", computerpoints)
            elif computerchoice == "P":
                print("You lost. Try again!")
                computerpoints += 1
                print("Result: User ", userpoints, " Computer ", computerpoints)
        if userchoice == "S":
            if computerchoice == "R":
                print("You lost. Try again!")
                computerpoints += 1
                print("Result: User ", userpoints, " Computer ", computerpoints)
            elif computerchoice == "P":
                print("You won! Scissors cut Paper!")
                userpoints += 1
                print("Result: User ", userpoints, " Computer ", computerpoints)
        else:
            if computerchoice == "S":
                print("You lost!")
                computerpoints += 1
                print("Result: User ", userpoints, " Computer ", computerpoints)
            elif computerchoice == "R":
                print("You won! Paper wraps Rock!")
                userpoints += 1
                print("Result: User ", userpoints, " Computer ", computerpoints)
    if computerpoints >= 2 and computerpoints > userpoints and i == 2:
        print("You lost the match!")
    elif userpoints >= 2 and userpoints > computerpoints and i == 2:
        print("You won the match!")
    elif userpoints == computerpoints and i == 2:
        print("It's a draw!")






