import random

moves=['rock', 'paper', 'scissors']

def calc_scores(your_move, my_move):
    if ((your_move == "paper" and my_move == "scissors") or
        (your_move == "rock" and my_move == "paper") or
        (your_move == "scissors" and my_move == "rock")):
        print(">>>>>>> i won!")
    else:
        print(">>>>>>> you won!")

def lets_play(move):
    print(">>>>>>> lets game rock, paper, scissors!")
    if (move in moves) :
        my_move = random.choice(moves)
        print(">>>>>>> your move: ", move)
        print(">>>>>>> my move: ", my_move)
        if (my_move == move):
            print(">>>>>>> its a tie!")
        else:
            scores = calc_scores(move, my_move)
    else:
        print(">>>>>>> please choose another option")


if __name__ == "__main__":
    import sys
    lets_play(str(sys.argv[1]))
