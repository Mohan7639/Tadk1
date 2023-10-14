from random import randint

moves = ["Rock", "Paper", "Scissor"]

while True:
    computer = moves[randint(0, 2)]
    player = input("Rock, Paper, or Scissor? (or type 'end' to quit)")

    if player.lower() == "end":
        print("The game has ended.")
        break
    elif player not in moves:
        print("Invalid move. Please enter Rock, Paper, or Scissor.")
    elif player == computer:
        print("It's a tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose! Paper beats Rock.")
        else:
            print("You win! Rock beats Scissor.")
    elif player == "Paper":
        if computer == "Scissor":
            print("You lose! Scissor beats Paper.")
        else:
            print("You win! Paper beats Rock.")
    elif player == "Scissor":
        if computer == "Rock":
            print("You lose! Rock beats Scissor.")
        else:
            print("You win! Scissor beats Paper.")
