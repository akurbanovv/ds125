# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : Akhmad Kurbanov
# Collaborators : Daria Menea
# Time spent    : ~10 hours
# 
# It successfully passed all the test-cases from the test file 
# (test_ps3.py). Also, I tested methods with my own inputs and it 
# also worked. I made a line separation between hand plays longer, 
# so it is easier to read output on the terminal. 

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7
ASTERISK = '*'

SCRABBLE_LETTER_VALUES = {
    '*': 0, 'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10,
}

# -----------------------------------
# Helper code

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    # print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    # print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    sum_of_points = 0  
    word_len = len(word) 

    # geting the sum of points for letter in the word
    for letter in word:
        sum_of_points += SCRABBLE_LETTER_VALUES.get(letter.lower())

    # calculating two components of the equation to get score
    first_com = sum_of_points
    second_com = (7 * word_len - 3 * (n - word_len))

    # calcuting word score
    if second_com > 1: score = first_com * second_com
    else: score = first_com * 1

    return score 

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    num_vowels = int(math.ceil(n / 3))

    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1

    # replacing a vowel with asterisk "*""
    for letter in hand:
        if letter in VOWELS and hand[letter] == 1: 
            del(hand[letter])
            hand[ASTERISK] = 1
            break

    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    updated_hand = hand.copy() # making a copy as hand is immutable
    word = word.lower()        # make letters in word lower case

    # delete letters from the hand which appeared in the word 
    for letter in word:
        if letter in updated_hand:
            if updated_hand[letter] != 0: updated_hand[letter] -= 1
    
    return updated_hand

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """

    word = word.lower()                  # make word lower case
    hand_copy = hand.copy()              # make a copy of the hand
    asterisk_index = word.find(ASTERISK) # index of "*"
    last_vowel = 'u'                     # last vowel in VOWEL

    # check if each letter of the word in hand 
    for letter in word:
        if letter in hand_copy:
            if hand_copy[letter] != 0: hand_copy[letter] -= 1
            else: return False 
        else: return False  

    # check if a word with asterisk or not (if it is not, index is -1)
    if asterisk_index > -1:
        # if it is with asterisk, change it with a vowel to see if its a word
        for vowel in VOWELS:
            word_to_check = word.replace(ASTERISK, vowel)
            if word_to_check in word_list: return True 
            elif vowel == last_vowel: return False
    else: return word in word_list

    return True         
    
    
#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    handlen = 0
    for freq in hand.values():
        handlen += freq
    return handlen

def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    
    total_score = 0             
    n = calculate_handlen(hand)     # amount of letters in hand 
    
    # keep playing a hand until it has letters 
    while n > 0:
        print("Current Hand: ", end = '')
        display_hand(hand)
        input_word = input('Enter word, or "!!" to indicate that you are finished: ') 

        if input_word == '!!': break
        else: 
            if is_valid_word(input_word, hand, word_list):
                
                # get score of the input word and add to total one 
                input_word_score = get_word_score(input_word, n)
                total_score += input_word_score

                print('"' + input_word + '"' + " earned " + str(input_word_score) 
                + " points. Total: " + str(total_score) + " points"'\n')

            else: print("That is not a valid word. Please choose another word."'\n')

        # delete letters from the hand which were used in input word
        hand = update_hand(hand, input_word)
        n = calculate_handlen(hand)

        # if hand doesn'have letters left 
        if n == 0: 
            print("Ran out of letters")
            return total_score
                
    return total_score

#
# Problem #6: Playing a game
# 
def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """

    hand_copy = hand.copy()
    alphabet = 'aeioubcdfghjklmnpqrstvwxyz'

    # check if letter to delete in the hand
    if letter in hand: 
        # save letter's frequency to assing to new letter
        letter_freq = hand_copy[letter]
        
        # keep searching while letter to add wasn't in hand before
        letter_to_add = letter
        while letter_to_add in hand:
            letter_to_add = random.choice(alphabet)

        # delete the letter and add a new letter with freq. of old letter
        del(hand_copy[letter])
        hand_copy[letter_to_add] = letter_freq

    return hand_copy
    
def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    
    total_score = 0
    letter_substituted = False
    hand_replayed = False
    yes = 'yes'
    no = 'no'

    number_of_hands = int(input("Enter total number of hands: "))
   
    # keep playing until we played all the hands
    while number_of_hands > 0:
        hand = deal_hand(HAND_SIZE) # create a hand with a hand size
        original_hand = hand.copy() # save initial hand for raplaying in the future

        # avoid printing out current hand two times 
        if not letter_substituted: 
            print("Current Hand: ", end = '')
            display_hand(hand)

        current_score = 0 # score of the current hand 

        # check if a letter was substituted before
        if not letter_substituted:
            check_substitution = input("Would you like to substitute a letter? ")
            
            if check_substitution == yes:
                letter_to_substitute = input("Which letter would you like to replace: ")
                print()
                hand = substitute_hand(hand, letter_to_substitute)
                letter_substituted = True
            elif check_substitution == no:
                print()

        # plat the hand
        current_score = play_hand(hand, word_list)
        print("Total score for this hand:", current_score)
        print("----------------------------------------------------------")
        
        # check if a letter was replayed before
        if not hand_replayed:
            check_replay = input("Would you like to replay the hand? ")

            if check_replay == yes:
                print()
                replayed_score = play_hand(original_hand, word_list)
                print("Total score for this hand:", replayed_score)
                print("----------------------------------------------------------")
                hand_replayed = True
                current_score = max(current_score, replayed_score)
            elif check_replay == no:
                print()
        
        # update total score and decrease # of hands
        total_score += current_score
        number_of_hands -= 1

    print("Total score over all hands:", total_score)

#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
