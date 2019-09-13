# Problem Set 2, hangman.py
# Name: Akhmadjon Kurbanov
# Collaborators: None
# Time spent: 8 hours

# Hangman Game
#
# Hangman implements a user-compuer interaction game. I spent 
# sufficient time testing each function and passed all my own 
# test cases and ones which were collaboratively developed by 
# the whole class. I created total of 12 test-cases for different 
# parts of this assignment; they all can be found in test_hangman.py
# I also developed my own version of the hangman, which is called
# my_hangman and can be found below. To play my version of the hangman
# you have to uncomment the last two lines of the code below (line 563). 
# -----------------------------------

import random
import string

WORDLIST_FILENAME = "words.txt"

# Helper code

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    # print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    # print("  ", len(wordlist), "words loaded.")
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
    # if each letter in secret word is not guessed yet, return false
    for letter in secret_word:
      if letter not in letters_guessed:
        return False
    return True



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed_word = []     

    # check each letter, if it is in letters_guessed, 
    # if it is append it to the list, otherwise append "_ "
    for letter in secret_word:
      if letter in letters_guessed:
        guessed_word.append(letter)
      else:
        guessed_word.append('_ ')

    guessed_word_to_string = ''.join(guessed_word)
    return guessed_word_to_string



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    letters_not_guessed = string.ascii_lowercase

    # removing each guessed letter from ascii string
    for letter in letters_guessed:
      if letter in letters_not_guessed:
        letters_not_guessed = letters_not_guessed.replace(letter, '')

    return letters_not_guessed
  
    
    
def hangman(secret_word):
    len_word = len(secret_word) 
    guesses_remaining = 6
    warnings_remaining = 3
    letters_guessed = []
    consonants = 'bcdfghjklmnpqrstvwxyz'
    vowels = 'aeiou'

    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(len_word) + " letters long.")
    print("You have 3 warnings left.")
    print("----------------------------------------------------------")

    # play the game until we have guesses left
    while guesses_remaining > 0:
      print("You have " + str(guesses_remaining) + " guesses left!")
      print("Available letters: " + get_available_letters(letters_guessed))
      
      letter_from_user = input("Please guess a letter: ").lower()
      
      # checking if letter is in alphabet
      if not letter_from_user.isalpha():
          warnings_remaining -= 1
          if warnings_remaining >= 0:
            print("Oops! That is not a valid letter. ")
            print("You have " + str(warnings_remaining) + " warnings left: " + get_guessed_word(secret_word, letters_guessed))
          else: 
            print("Oops! That is not a valid letter. ")
            print("You have no warnings left so you lose one guess: " + get_guessed_word(secret_word, letters_guessed))
            guesses_remaining -= 1

      # checking if user already guessed the letter 
      elif letter_from_user in letters_guessed:
          warnings_remaining -= 1
          if warnings_remaining >= 0:
            print("Oops! You've already guessed that letter. ") 
            print("You have " + str(warnings_remaining) + " warnings left: " + get_guessed_word(secret_word, letters_guessed))
          else: 
            print("Oops! You've already guessed that letter. ") 
            print("You have no warnings left so you lose one guess: " + get_guessed_word(secret_word, letters_guessed))
            guesses_remaining -= 1

      # checking if input is a single letter 
      elif len(letter_from_user) != 1: 
          warnings_remaining -= 1
          if warnings_remaining >= 0:
            print("Oops! You have to enter a single letter. ")
            print("You have " + str(warnings_remaining) + " warnings left: " + get_guessed_word(secret_word, letters_guessed))
          else: 
            print("Oops! You have to enter a single letter. ")
            print("You have no warnings left so you lose one guess: " + get_guessed_word(secret_word, letters_guessed))
            guesses_remaining -= 1

      # else letter is valid and was not guessed
      else:
          letters_guessed.append(letter_from_user)  
          
          if letter_from_user in secret_word:
            print("Good guess: " + get_guessed_word(secret_word, letters_guessed))
          else: 
            if letter_from_user in consonants: 
              guesses_remaining -= 1
            elif letter_from_user in vowels:
              guesses_remaining -= 2
            
            print("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
      
      print("----------------------------------------------------------")
      if is_word_guessed(secret_word, letters_guessed): break

    # calculating total score after the game is finished and the word is guessed
    if is_word_guessed(secret_word, letters_guessed): 
      num_of_letters = 0
      for letter in letters_guessed:
        if letter in secret_word: 
            num_of_letters += 1
      total_score = guesses_remaining * num_of_letters

      print("Congratulations, you won!")
      print("Your total score for this game is: " + str(total_score))
    else: 
      print("Sorry, you ran out of guesses. The word was " + secret_word + ".")



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
    # deleting the space after each underscore
    my_word = my_word.replace(' ', '')
    
    # checking length of each word
    if len(my_word) != len(other_word):
      return False
    
    # checking if each letter is equal to corresponding letter in each word
    for i in range(len(my_word)):
      if my_word[i] != '_':
        if my_word[i] != other_word[i]:
          return False
    
    # checking if the amount of each letter in each word is equal or not
    for letter in my_word:
      if letter != '_':
        if my_word.count(letter) != other_word.count(letter):
          return False
    
    return True



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.
    '''
    matches = []
    matched = False

    # append each word from the word list which matches my_word
    for word in wordlist:
      if match_with_gaps(my_word, word):
        matches.append(word)
        matched = True

    if matched: print(*matches, sep=" ")
    else: print("No matches found")
    


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    '''

    len_word = len(secret_word)
    guesses_remaining = 6
    warnings_remaining = 3
    letters_guessed = []
    consonants = 'bcdfghjklmnpqrstvwxyz'
    vowels = 'aeiou'

    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(len_word) + " letters long.")
    print("You have 3 warnings left.")
    print("----------------------------------------------------------")

    # play the game until we have guesses left
    while guesses_remaining > 0:
      print("You have " + str(guesses_remaining) + " guesses left!")
      print("Available letters: " + get_available_letters(letters_guessed))
      
      letter_from_user = input("Please guess a letter: ").lower()

      # if input is asterisk, show hints
      if letter_from_user == '*':
        show_possible_matches(get_guessed_word(secret_word, letters_guessed))
    
      # checking if letter is in alphabet
      elif not letter_from_user.isalpha():
          warnings_remaining -= 1
          if warnings_remaining >= 0:
            print("Oops! That is not a valid letter. ")
            print("You have " + str(warnings_remaining) + " warnings left: " + get_guessed_word(secret_word, letters_guessed))
          else:
            print("Oops! That is not a valid letter. ")
            print("You have no warnings left so you lose one guess: " + get_guessed_word(secret_word, letters_guessed))
            guesses_remaining -= 1

      # checking if user already guessed the letter 
      elif letter_from_user in letters_guessed:
          warnings_remaining -= 1
          if warnings_remaining >= 0:
            print("Oops! You've already guessed that letter. ") 
            print("You have " + str(warnings_remaining) + " warnings left: " + get_guessed_word(secret_word, letters_guessed))
          else: 
            print("Oops! You've already guessed that letter. ") 
            print("You have no warnings left so you lose one guess: " + get_guessed_word(secret_word, letters_guessed))
            guesses_remaining -= 1

      # checking if input is a single letter 
      elif len(letter_from_user) != 1: 
          warnings_remaining -= 1
          if warnings_remaining >= 0:
            print("Oops! You have to enter a single letter. ")
            print("You have " + str(warnings_remaining) + " warnings left: " + get_guessed_word(secret_word, letters_guessed))
          else: 
            print("Oops! You have to enter a single letter. ")
            print("You have no warnings left so you lose one guess: " + get_guessed_word(secret_word, letters_guessed))
            guesses_remaining -= 1

      # at this point letter is a valid letter
      else:
          letters_guessed.append(letter_from_user)  
          
          if letter_from_user in secret_word:
            print("Good guess: " + get_guessed_word(secret_word, letters_guessed))
          else: 
            if letter_from_user in consonants: 
              guesses_remaining -= 1
            elif letter_from_user in vowels:
              guesses_remaining -= 2
            
            print("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
      
      print("----------------------------------------------------------")
      if is_word_guessed(secret_word, letters_guessed): break

     # calculating total score after the game is finished and the word is guessed
    if is_word_guessed(secret_word, letters_guessed): 
      num_of_letters = 0
      for letter in letters_guessed:
        if letter in secret_word: 
            num_of_letters += 1
      total_score = guesses_remaining * num_of_letters

      print("Congratulations, you won!")
      print("Your total score for this game is: " + str(total_score))
    else: 
      print("Sorry, you ran out of guesses. The word was " + secret_word + ".")
    


# -----------------------------------



def show_hangman_pic(guesses):
    hangman = (
    """
    -----
    |   |
    |
    |
    |
    |
    |
    |
    |
    --------
    """,
    """
    -----
    |   |
    |   0
    |
    |
    |
    |
    |
    |
    --------
    """,
    """
    -----
    |   |
    |   0
    |  -+-
    |
    |
    |
    |
    |
    --------
    """,
    """
    -----
    |   |
    |   0
    | /-+-\ 
    |
    |
    |
    |
    |
    --------
    """,
    """
    -----
    |   |
    |   0
    | /-+-\ 
    |   | 
    |   | 
    |
    |
    |
    --------
    """,
    """
    -----
    |   |
    |   0
    | /-+-\ 
    |   | 
    |   | 
    |  | 
    |  | 
    |
    --------
    """,
    """
    -----
    |   |
    |   0
    | /-+-\ 
    |   | 
    |   | 
    |  | | 
    |  | | 
    |
    --------
    """)
    print(hangman[guesses])



def my_hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    '''

    len_word = len(secret_word)
    guesses_remaining = 6
    old_gusses_reamaining = guesses_remaining
    warnings_remaining = 3
    letters_guessed = []
    consonants = 'bcdfghjklmnpqrstvwxyz'
    vowels = 'aeiou'

    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(len_word) + " letters long.")
    print("You have 3 warnings left.")
    show_hangman_pic((guesses_remaining+1)*(-1))
    print("----------------------------------------------------------")

    # play the game until we have to guesses left
    while guesses_remaining > 0:
      print("You have " + str(guesses_remaining) + " guesses left!")
      print("Available letters: " + get_available_letters(letters_guessed))
      
      letter_from_user = input("Please guess a letter: ").lower()

      # checking if input is asterisk to get hints
      if letter_from_user == '*':
        show_possible_matches(get_guessed_word(secret_word, letters_guessed))
      
      # checking if letter is in alphabet
      elif not letter_from_user.isalpha():
          warnings_remaining -= 1
          if warnings_remaining >= 0:
            print("Oops! That is not a valid letter. ")
            print("You have " + str(warnings_remaining) + " warnings left: " + get_guessed_word(secret_word, letters_guessed))
          else:
            print("Oops! That is not a valid letter. ")
            print("You have no warnings left so you lose one guess: " + get_guessed_word(secret_word, letters_guessed))
            guesses_remaining -= 1

      # checking if user already guessed the letter 
      elif letter_from_user in letters_guessed:
          warnings_remaining -= 1
          if warnings_remaining >= 0:
            print("Oops! You've already guessed that letter. ") 
            print("You have " + str(warnings_remaining) + " warnings left: " + get_guessed_word(secret_word, letters_guessed))
          else: 
            print("Oops! You've already guessed that letter. ") 
            print("You have no warnings left so you lose one guess: " + get_guessed_word(secret_word, letters_guessed))
            guesses_remaining -= 1

      # checking if the input is a single letter 
      elif len(letter_from_user) != 1: 
          warnings_remaining -= 1
          if warnings_remaining >= 0:
            print("Oops! You have to enter a single letter. ")
            print("You have " + str(warnings_remaining) + " warnings left: " + get_guessed_word(secret_word, letters_guessed))
          else: 
            print("Oops! You have to enter a single letter. ")
            print("You have no warnings left so you lose one guess: " + get_guessed_word(secret_word, letters_guessed))
            guesses_remaining -= 1

      # at this point input is a valid letter
      else:
          letters_guessed.append(letter_from_user)  
          
          if letter_from_user in secret_word:
            print("Good guess: " + get_guessed_word(secret_word, letters_guessed))
          else: 
            if letter_from_user in consonants: 
              guesses_remaining -= 1
            elif letter_from_user in vowels:
              guesses_remaining -= 2
            
            print("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
      
      # if amount of guesses left changed, print out the picture
      if old_gusses_reamaining > guesses_remaining:
        # getting the right index of the hangman in the pack of pictures
        show_hangman_pic((guesses_remaining+1)*(-1))
        old_gusses_reamaining = guesses_remaining
      print("----------------------------------------------------------")
      if is_word_guessed(secret_word, letters_guessed): break

    #  # calculating total score after the game is finished and the word is guessed
    if is_word_guessed(secret_word, letters_guessed): 
      num_of_letters = 0
      for letter in letters_guessed:
        if letter in secret_word: 
            num_of_letters += 1
      total_score = guesses_remaining * num_of_letters

      print("Congratulations, you won!")
      print("Your total score for this game is: " + str(total_score))
    else: 
      print("Sorry, you ran out of guesses. The word was " + secret_word + ".") 



if __name__ == "__main__":
  # secret_word = choose_word(wordlist)
  # hangman(secret_word)

###############

  secret_word = choose_word(wordlist)
  hangman_with_hints(secret_word)

###############

  # I added a modification into the game, commentout two lines 
  # above and uncomment two lines below to check it out.   

  # secret_word = choose_word(wordlist)
  # my_hangman(secret_word)
