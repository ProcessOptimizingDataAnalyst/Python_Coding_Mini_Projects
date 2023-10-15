import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words) # randomly chooses something from the list
    while '_' in word or ' ' in word:
        word =  random.choice(words)

    return word.upper()

def hangman(): # the below will allow us to keep track of the valid letter
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # What the user has guessed

    lives = 6 # this is the # of lives/chances the user has for guessing
    
    # getting user input
    while len(word_letters)> 0 and lives > 0: # 'len(word_letters)> 0' = while this conditon applies you're going to continue iterating through the input below until the user gets all the letters + 'lives > 0' = while the user's life is not 0, so they haven't died 6 times, the loop, the condition below applies
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters)) # this line will let us know which charcters we already used

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '_' for letter in word] # The current letter the user guessed will be shown while the other letters will be in dashes
        print('Current word: ', ' '.join(word_list)) # then you take the list above and join it with word_list, just like above

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters: # if this a valid charavter in the alphabet variable I haven't used yet
            used_letters.add(user_letter) # you'll add the used_letters set
            if user_letter in word_letters:
                word_letters.remove(user_letter)# everytime a user_letter is in the word_letters list from word.py,  we remove the specific word_letters

            else: # when users don't guess the right letter, a life is taken away from them
                lives = lives - 1 # take away a life if wrong
                print('Letter is not in word')
                
        elif user_letter in used_letters:
            print('You have already used that character. Please try again.')# this means that the user already used a specific letter; i.e. that's an invalid guess
        else: # i.e. the charcater you typed is not in the word.py OR is not a charcater you already used.
            print('Imvalid character. Please try again!')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print('You died, sorry. The word was', word)
    else:
        print('You guessed the word', word, '!!')


hangman()
