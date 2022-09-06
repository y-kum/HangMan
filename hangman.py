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
    h = 0
    for char1 in secret_word:
        for char2 in letters_guessed:
            if char1 == char2:
                h = h + 1
                break
    return h == len(secret_word)

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    l = []
    for char1 in secret_word:
        h = len(l)
        for char2 in letters_guessed:
            if char1 == char2:
                l.append(char1)
                break
        if len(l) > h:
            pass
        else:
            l.append('_ ')

    s1 = ''.join(l)
    return s1

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    import string
    s1 = string.ascii_lowercase
    l1 = list(s1)
    for char1 in s1:
        for char2 in letters_guessed:
            if char1 == char2:
                l1.remove(char1)
                break
    s2 = ''.join(l1)

    return s2


def repeated_word(letter_guessed, letters_guessed):
    z = 0
    for char in letters_guessed:
        if char == letter_guessed:
            z = 1
            break
        else:
            z = 0

    return z == 1

# secret_word = choose_word(wordlist)
secret_word = 'else'
letters_guessed = []
letter_guessed= []
a = is_word_guessed(secret_word, letters_guessed)
b = get_guessed_word(secret_word, letters_guessed)
c = get_available_letters(letters_guessed)
j = repeated_word(letter_guessed, letters_guessed)

# print (secret_word)
# print(a)
# print(b)
# print(c)

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    d = 6
    e = 3
    f = 0
    print('Welcome to the Hangman!')
    print('I am thinking of a word that is', len(secret_word), 'letters long.')
    print('---------------------------------------------------------------------')
    print('You have', d, 'guesses left.')
    print('Available letters:', c)


    while d > 0:

        b = get_guessed_word(secret_word, letters_guessed)
        letter_guessed = input('Please guess a letter:')
        letter_guessed = letter_guessed.lower()
        s_l = ''.join(letter_guessed)
        j = repeated_word(letter_guessed, letters_guessed)

        if  s_l.isalpha() != True:
            e = e-1
            k = get_guessed_word(secret_word, letters_guessed)
            l = get_available_letters(letters_guessed)
            if e >= 0:
                print('---------------------------------------------------------------------')
                print('Oops! That is not a valid letter. You have', e, 'warnings left.', k)
                print('You have', d, 'guesses left.')
                print('Available letters:', l)

            else:
                d = d-1
                print('---------------------------------------------------------------------')
                print('Oops! That is not a valid letter.', k)
                print('You have no warnings left so you lose one guess. You have', d, 'guesses left.')
                print('Available letters:', l)



        elif (s_l.isalpha() == True) and (j != True):


            letters_guessed.append(letter_guessed)
            print('---------------------------------------------------------------------')

            k = get_guessed_word(secret_word, letters_guessed)
            l = get_available_letters(letters_guessed)

            if k != b:
                f = f+1
                print('Good guess:', k)
                print('You have', d, 'guesses left.')
                print('Available letters:', l)
            elif ((letter_guessed == 'a') or (letter_guessed == 'e') or (letter_guessed == 'i') or (letter_guessed == 'o') or (letter_guessed == 'u')):
                d = d-2
                print('Oops! That letter is not in my word:', k)
                print('You have', d, 'guesses left.')
                print('Available letters:', l)
            else:
                d = d - 1
                print('Oops! That letter is not in my word:', k)
                print('You have', d, 'guesses left.')
                print('Available letters:', l)


        elif (s_l.isalpha() == True) and (j == True):
            e = e - 1
            k = get_guessed_word(secret_word, letters_guessed)
            l = get_available_letters(letters_guessed)
            if e >= 0:
                print('---------------------------------------------------------------------')
                print('Oops! You have already guessed that letter. You have', e, 'warnings left.', k)
                print('You have', d, 'guesses left.')
                print('Available letters:', l)

            else:
                d = d - 1
                print('---------------------------------------------------------------------')
                print('Oops! You have already guessed that letter.', k)
                print('You have no warnings left so you lose one guess. You have', d, 'guesses left.')
                print('Available letters:', l)

        v = is_word_guessed(secret_word, letters_guessed)
        if v == True :
            score = (d*f)
            print('---------------------------------------------------------------------')
            print('Congratulations, you won!')
            print('Your total score for this game is:', score)
            break

    if (d == 0) or (d < 0):
        print('Sorry! You ran out of guesses. The word was:', secret_word)


    return 'Lets play again!'


# print(hangman(secret_word))


########################################################

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
    p = get_guessed_word(other_word, letters_guessed)
    return p == my_word


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    n = []
    for x in wordlist:
        if len(x) == len(secret_word):
            n.append(x)

    m = []
    for x in n:
        other_word = x
        my_word = get_guessed_word(secret_word, letters_guessed)
        f = match_with_gaps(my_word, other_word)
        if f == True:
            m.append(x)
    print(m)

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
    d = 6
    e = 3
    f = 0
    print('Welcome to the Hangman!')
    print('I am thinking of a word that is', len(secret_word), 'letters long.')
    print('---------------------------------------------------------------------')
    print('You have', d, 'guesses left.')
    print('Available letters:', c)

    while d > 0:

        b = get_guessed_word(secret_word, letters_guessed)
        letter_guessed = input('Please guess a letter:')
        letter_guessed = letter_guessed.lower()
        s_l = ''.join(letter_guessed)
        j = repeated_word(letter_guessed, letters_guessed)

        if (s_l.isalpha() != True) and (s_l != '*'):
            e = e - 1
            k = get_guessed_word(secret_word, letters_guessed)
            l = get_available_letters(letters_guessed)
            if e >= 0:
                print('---------------------------------------------------------------------')
                print('Oops! That is not a valid letter. You have', e, 'warnings left.', k)
                print('You have', d, 'guesses left.')
                print('Available letters:', l)

            else:
                d = d - 1
                print('---------------------------------------------------------------------')
                print('Oops! That is not a valid letter.', k)
                print('You have no warnings left so you lose one guess. You have', d, 'guesses left.')
                print('Available letters:', l)

        elif s_l == '*':
            my_word = get_guessed_word(secret_word, letters_guessed)
            n = show_possible_matches(my_word)
            l = get_available_letters(letters_guessed)

            print('---------------------------------------------------------------------')
            print('Possible word matches are:',
                  n)
            print('You have', d, 'guesses left.')
            print('Available letters:', l)



        elif (s_l.isalpha() == True) and (j != True):

            letters_guessed.append(letter_guessed)
            print('---------------------------------------------------------------------')

            k = get_guessed_word(secret_word, letters_guessed)
            l = get_available_letters(letters_guessed)

            if k != b:
                f = f + 1
                print('Good guess:', k)
                print('You have', d, 'guesses left.')
                print('Available letters:', l)
            elif ((letter_guessed == 'a') or (letter_guessed == 'e') or (letter_guessed == 'i') or (
                    letter_guessed == 'o') or (letter_guessed == 'u')):
                d = d - 2
                print('Oops! That letter is not in my word:', k)
                print('You have', d, 'guesses left.')
                print('Available letters:', l)
            else:
                d = d - 1
                print('Oops! That letter is not in my word:', k)
                print('You have', d, 'guesses left.')
                print('Available letters:', l)


        elif (s_l.isalpha() == True) and (j == True):
            e = e - 1
            k = get_guessed_word(secret_word, letters_guessed)
            l = get_available_letters(letters_guessed)
            if e >= 0:
                print('---------------------------------------------------------------------')
                print('Oops! You have already guessed that letter. You have', e, 'warnings left.', k)
                print('You have', d, 'guesses left.')
                print('Available letters:', l)

            else:
                d = d - 1
                print('---------------------------------------------------------------------')
                print('Oops! You have already guessed that letter.', k)
                print('You have no warnings left so you lose one guess. You have', d, 'guesses left.')
                print('Available letters:', l)

        v = is_word_guessed(secret_word, letters_guessed)
        if v == True:
            score = (d * f)
            print('---------------------------------------------------------------------')
            print('Congratulations, you won!')
            print('Your total score for this game is:', score)
            break

    if (d == 0) or (d < 0):
        print('Sorry! You ran out of guesses. The word was:', secret_word)

    return 'Lets play again!'

    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.

#
if __name__ == "__main__":
#     # pass
#
#     # To test part 2, comment out the pass line above and
#     # uncomment the following two lines.
#
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
