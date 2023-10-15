import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r','p','s'])

    if user == computer: # i.e. if the outcome of the code exectuion represents a situation where the value of the user variable is EQUUAL to the value in computer
        return 'It\'s a tie'

    # r > s, s > p, p > r
    if is_win(user,computer): # i.e. if the outcome of the code exectuion represents a situation similr to the conditons listed in the 'is_win' function
        return 'You won!'

    return 'You lost!'

def is_win(player, opponent):
    # return true if the player wins
    # r > s, s > p, p > r
        if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p')\
           or (player == 'p' and opponent == 'r'):
            return True # 'return True' means that the condition above (.e. '(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p')\
                           ## or (player == 'p' and opponent == 'r')' ) has been realised AND this means that the player has won

print(play())
        

