import random

def guess(x):
    random_number = random.randint(1, x) # The randint() method returns an integer number selected element from the specified range.
    guess = 0
    while guess != random_number:
        guess = int(input(f'guess a number between 1 and {x} '))
        if guess < random_number:
            print('Sorry, guess again. Too low!')
        elif guess > random_number:
            print('Sorry, guess again. Too high!')


    print(f'Yay, congrats. You have guessed the number {random_number} correctly !!!!')

guess(10)
        
