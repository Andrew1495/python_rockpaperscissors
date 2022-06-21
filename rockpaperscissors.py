
play_game =input("Hellow would you like to play rock, paper, scissors ? ".lower())

if play_game != "yes":
    print("shutdown!")
    quit()
player_score = 0
computer_score = 0
tie_score = 0
player = str()

def valid_input(player):
    player = input("rock paper or scissors ? ".lower())
    while player != "paper" and player != "rock" and player != "scissors":
        print("please enter rock paper or scissors")
        player = input("rock paper or scissors ? ".lower())
    else:
        return player


while (player_score < 5 and computer_score < 5 ):
    player_choice = valid_input(player)
    

    import random
    computer_number = random.randint(1, 3)


    if computer_number == 1:
        computer_choice = "rock"

    elif computer_number == 2:
        computer_choice = "paper"

    elif computer_number == 3:
        computer_choice = "scissors"

    print("Computer selected", computer_choice)
    print("You selected", player_choice)


    if (player_choice == "rock" and computer_choice == "rock"):
        print("draw")
        tie_score += 1
    elif (player_choice == "paper" and computer_choice == "paper"):
        print("draw")
        tie_score += 1
    elif (player_choice == "scissors" and computer_choice == "scissors"):
        print("draw")
        tie_score += 1
    elif (player_choice == "rock" and computer_choice == "paper"):
        print("You Lose")
        computer_score += 1

    elif (player_choice == "rock" and computer_choice == "scissors"):
        print("You Win")
        player_score += 1
    elif (player_choice == "paper" and computer_choice == "scissors"):
        print("You Lose")
        computer_score += 1
    elif (player_choice == "paper" and computer_choice == "rock"):
        print("You Win")
        player_score += 1
    elif (player_choice == "scissors" and computer_choice == "rock"):
        print("You Lose")
        computer_score += 1
    elif (player_choice == "scissors" and computer_choice == "paper"):
        print("You Win")
        player_score += 1


    print("Computer Score: ",computer_score,"Your Score: ",player_score,"Tied games: ",tie_score)

while player_score == 5: 
    print("YOU WIN!!!")
    quit()

while computer_score == 5:
    print("YOU LOSE!!!")
    quit()

else:
    quit()



