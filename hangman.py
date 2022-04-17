# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for letter in secret_word:
        if not(letter in letters_guessed):
            return False
    return True



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guessed_word = ""
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word += letter
        else:
            guessed_word += "_ "
    return guessed_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    available_letters = ""
    for letter in string.ascii_lowercase:
        if not(letter in letters_guessed):
            available_letters += letter
    return available_letters
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    *1 At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    *2 The user should start with 6 guesses

    *3 Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    *4 Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    *5 The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    *6 After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    letters_guessed = ""
    #2
    num_guesses = 6
    # 3 warnings for user entering invalid input.
    num_warnings = 3
    print("Welcome to the game Hangman!")
    #1
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    while not(is_word_guessed(secret_word, letters_guessed)):
        if num_guesses == 0:
            break
        #3
        print("You have", num_warnings, "warnings left.")
        print("You have", num_guesses, "guesses left.")
        # show to user the available letters for guessing
        print(get_available_letters(letters_guessed))
        #4
        user_guesses = str.lower(input("Please guess a letter: "))
        # if user enters invalid input such as non alphabets, subtract 1 warning or 1 guess.
        if not(str.isalpha(user_guesses)):
            # I offer 3 warnings to the user for entering invalid input.
            if num_warnings != 0:
                num_warnings -= 1
                print("Oops! That is not a valid letter. You have", num_warnings, "warnings left,", get_guessed_word(secret_word, letters_guessed))
            # if user enters invalid input after run out of warnings, subtract 1 guess.
            else:
                num_guesses -= 1
                print("Oops! That is not a valid letter. You have", num_guesses, "guesses left", get_guessed_word(secret_word, letters_guessed))
            # when there's no warnings left, subtract one guess
            if num_warnings < 0:
                num_guesses -= 1
        # if user enters invalid input such as letters_guessed, subtract 1 warning or 1 guess.
        elif user_guesses in letters_guessed:
            if num_warnings != 0:
                num_warnings -= 1
                print("Oops! You've already guessed that letter. You now have", num_warnings, "warnings:")
            else:
                num_guesses -= 1
                print("Oops! You've already guessed that letter. You now have", num_guesses, "guesses:")
            print(get_guessed_word(secret_word, letters_guessed))
        # if user enters valid input, run the game as follow.
        else:
            # keep track of letters_guessed
            letters_guessed += user_guesses
            # after each guess, display to user which letter in secret_word is guessed
            # and unguessed letter replaces with an (_ ).
            if user_guesses in secret_word:
                print("Good guess:", get_guessed_word(secret_word, letters_guessed))
                # if the user guessed a letter that is in secret word, user lose no guess.
            else:
                print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
                # if user enters any vowel that is not in secret_word, subtract 2 guesses.
                if user_guesses in "aeiou":
                    num_guesses -= 2
                # if user enters consonant that is not in secret_word, subtract 1 guess.
                else:
                    num_guesses-=1
                

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    secret_word = "abcefg"
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
