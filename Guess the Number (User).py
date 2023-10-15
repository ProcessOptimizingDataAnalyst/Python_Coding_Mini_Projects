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

def computer_guess(x): # we're not going to tell the PC the #, so the PC will have a range of # to work with; a min & max
        low = 1 # this is the lower bound
        high = x
        feedback = ''
        while feedback != 'c': # we're looping back into the 'feedback' variable + 'c' = correct
            if low!= high:
                guess = random.randint(low, high)
            else:
                guess = low # could also be high b/c low = high
            feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)??').lower()
            if feedback == 'h': # we're saying if it's/our guess is too high, we want to adjust our upper bound
                high = guess - 1 # the high bound is lower than the # we guessed by @ leat 1 unit; if our guess was for eg. '8' and we get a message stating that 8 is too high, then we know the correct answer is between 1~7
            elif feedback == 'l':
                low = guess + 1
            # if we guessed the right number; pour guess was correct, we don't need anelse statement becoz our while loop takes care of that
            ## When we exit our while loop; this means that the PC has guessed our # corrctly and we print the statement below:
        print(f'Yay! The computer guessed your number, {guess}, correctly!!')
computer_guess(10)
