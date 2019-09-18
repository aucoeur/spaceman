from random import choice

letters_guessed = []

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.

    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    # f = open('words.txt', 'r')
    # words_list = f.readlines()
    # f.close()

    with open('words.txt') as f:
        words_list = f.readlines()

    words_list = words_list[0].split(' ')
    secret_word = choice(words_list)
        
    return secret_word

def restart():
    while True:
        play = input('\nPlay again? Y/N: ').lower()
        if play == 'y' or play == 'yes':
            letters_guessed.clear()
            secret_word = load_word()
            spaceman(secret_word)
        elif play == 'n' or play == 'no':
            print('GOODBYE')
            quit()
        else:
            print('Invalid input.  Please enter Y or N. ')

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.

    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed

    reveal = [char for char in secret_word if char in letters_guessed]

    if len(reveal) == len(secret_word):
        return True
    else:
        return False

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.

    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
    answers = []

    for item in secret_word: 
        if item in letters_guessed:
        # Okay, so I realized this intersection is redundant but I got emotionally attached to it so I left it in because reasons
        # reveal = set(letters_guessed).intersection(secret_word)
        # if item in reveal:
            answers.append(item)
        else:
            answers.append('_')
    
    answer = ' '.join(answers)
    return 'Answer: ' + answer
      
def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word

    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word

    Returns:
        bool: True if the guess is in the secret_word, False otherwise

    '''
    #TODO: check if the letter guess is in the secret word
    if guess in secret_word and guess not in letters_guessed:
        letters_guessed.append(guess)
        print('\n>> YES ITS HERE.\n')
        return True
    elif guess in letters_guessed:
        print('\n>> YOU ALREADY GUESSED THAT LETTER\n')
        return False
    else:
        letters_guessed.append(guess)
        print('\n>> NOPE. ')
        letters_guessed.sort()
        print('>> Guessed letters: ', *letters_guessed, '\n')
        return False

def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.

    Args:
      secret_word (string): the secret word to guess.

    '''

    #TODO: show the player information about the game according to the project spec
    print('Welcome to Spaceman!')
    print('The secret word contains: ' + str(len(secret_word)) + ' letters')
    print('You have 7 incorrect guesses, please enter one letter per round')
    print('------------------------------------')

    #TODO: Ask the player to guess one letter per round and check that it is only one letter
    while True:
        guess = input('Enter a letter: ').lower()
        if len(guess) != 1:
            print('Please enter one letter at a time.')
        elif guess.isalpha() == False:
            print('THAT IS NOT A LETTER')
        else:
            #TODO: Check if the guessed letter is in the secret or not and give the player feedback
            is_guess_in_word(guess, secret_word)
            
            #TODO: show the guessed word so far
            get_guessed_word(secret_word, letters_guessed)
    
            #TODO: check if the game has been won or lost
            wrong = set(letters_guessed).difference(secret_word)   

            if is_word_guessed(secret_word, letters_guessed) == True:
                print('YOU JUST WON THE GAME')
                restart()
            elif len(wrong) > 6:
                print('YOU JUST LOST THE GAME \nThe word was: ' + secret_word)
                restart()
                return False
            else:
                print('Incorrect Guesses: ' + str(len(wrong)))

# These function calls that will start the game
if '__name__' == '__main__':
    running = True
    while running:
        secret_word = load_word()
        spaceman(secret_word)