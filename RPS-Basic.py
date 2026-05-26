import random

def is_win(player, opponent):
    return (
        (player == 'r' and opponent == 's') or
        (player == 's' and opponent == 'p') or
        (player == 'p' and opponent == 'r')
    )

def play():
    wins = 0
    losses = 0
    ties = 0

    while True:
        user = input("Type r for rock, p for paper, s for scissors, or q to quit: ").lower()

        if user == 'q':
            print("Goodbye!")
            break

        if user not in ['r', 'p', 's']:
            print("Error 400 (Bad Request)")
            print("Try a different input")
            continue

        computer = random.choice(['r', 'p', 's'])
        print(f"Computer chose {computer}")

        if user == computer:
            print("It's a tie!")
            ties += 1
        elif is_win(user, computer):
            print("You win!")
            wins += 1
        else:
            print("You lose!")
            losses += 1

        print(f"Wins: {wins} | Losses: {losses} | Ties: {ties}\n")

play()
