from hangman import *

# Problem Set 3, test_hangman.py
# Name: Akhmadjon Kurbanov
# Collaborators: N/A
# Time spent: 2

def test_is_word_guessed(): 
    print('Testing is_word_guessed\n')

    # test 1 - with one letter not in guessed letters  
    secret_word = 'table'
    letters_guessed = ['t', 'a', 'o', 'l', 'e', 's']

    if is_word_guessed(secret_word, letters_guessed):
        print('FAILURE: is_word_guessed() with one letter not in guessed letters')
        print('\t Expected "False", but got ' + is_word_guessed(secret_word, letters_guessed))
    else: print('SUCCESS: is_word_guessed() with one letter not in guessed letters')
    
    # test 2 - with few letters not in guessed letters
    secret_word = 'horse'
    letters_guessed = ['a', 'v', 'o', 'l', 'e', 's']

    if is_word_guessed(secret_word, letters_guessed):
        print('FAILURE: is_word_guessed() with few letters not in guessed letters')
        print('\t Expected "False", but got ' + is_word_guessed(secret_word, letters_guessed))
    else: print('SUCCESS: is_word_guessed() with few letters not in guessed letters')

    # test 3 - with all letters not in guessed letters
    secret_word = 'horse'
    letters_guessed = ['g', 'q', 'a', 'j', 'i', 'z']

    if is_word_guessed(secret_word, letters_guessed):
        print('FAILURE: is_word_guessed() with all letters not in guessed letters')
        print('\t Expected "False", but got ' + is_word_guessed(secret_word, letters_guessed))
    else: print('SUCCESS: is_word_guessed() with all letters not in guessed letters')

def test_get_guessed_word():
    print('Testing get_guessed_word()\n')
    
    # test 1 - when all letters are guessed 
    secret_word = 'house' 
    letters_guessed = ['h', 'u', 'o', 'l', 'e', 's']
    guessed_word = get_guessed_word(secret_word, letters_guessed)
    
    if guessed_word != 'house':
        print('FAILURE: test_get_guessed_word() with all letters guessed')
        print('\t Expected "house", but got ' + guessed_word)
    else: print('SUCCESS: test_get_guessed_word() with all letters guessed')

    # test 2 - when only few letters are guessed
    secret_word = 'apple'
    letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
    guessed_word = get_guessed_word(secret_word, letters_guessed)

    if guessed_word != '_ pp_ e':
        print('FAILURE: test_get_guessed_word() with few letters guessed')
        print('\t Expected "_ pp_ e", but got ' + guessed_word)
    else: print('SUCCESS: test_get_guessed_word() with few letters guessed')
    
    # test 3 - when no letters are guessed
    secret_word = 'laptop' 
    letters_guessed = ['f', 'i', 'v', 'g', 'j', 'q']
    guessed_word = get_guessed_word(secret_word, letters_guessed)
    
    if guessed_word != '_ _ _ _ _ _ ':
        print('FAILURE: test_get_guessed_word() with no letters guessed')
        print('\t Expected "_ _ _ _ _ _ ", but got ' + guessed_word)
    else: print('SUCCESS: test_get_guessed_word() with no letters guessed')

def test_get_available_letters():
    print('Testing get_available_letters()\n')

    # test 1 with some letters guessed
    letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
    if get_available_letters(letters_guessed) != 'abcdfghjlmnoqtuvwxyz':
        print('FAILURE: test_get_available_letters() with some letters guessed')
    else: print('SUCCESS: test_get_available_letters() with some letters guessed')

    # test 2 with no letters guessed
    letters_guessed = []
    if get_available_letters(letters_guessed) != 'abcdefghijklmnopqrstuvwxyz':
        print('FAILURE: test_get_available_letters() with no letters guessed')
    else: print('SUCCESS: test_get_available_letters() with no letters guessed')

    # test 3 with numbers in letter guessed
    letters_guessed = ['b', 'd', 'z', 's', 'v', '9', 'g']
    if get_available_letters(letters_guessed) != 'acefhijklmnopqrtuwxy':
        print('FAILURE: test_get_available_letters() with a number in letter guessed')
    else: print('SUCCESS: test_get_available_letters() with a number in letter guessed')

def test_match_with_gaps():
    print('Testing match_with_gaps()\n')
    
    # test 1 with matching words 
    my_word = 's_ h_ _ l'
    other_word = 'school'
    if match_with_gaps(my_word, other_word) != True:
        print('FAILURE: test_match_with_gaps() with matching words')
        print('\t Expected True, but got ' + my_word)
    else: print('SUCCESS: test_match_with_gaps() with matching words')

    # test 2 when words have different amount of letters
    my_word = 'pi_ k'
    other_word = 'bottle'
    if match_with_gaps(my_word, other_word) != False:
        print('FAILURE: test_match_with_gaps() when words have diff. amount of letters')
        print('\t Expected False, but got ' + my_word)
    else: print('SUCCESS: test_match_with_gaps() when words have diff. amount of letters')

    # test 3 when gussed letter appears less times than it should 
    my_word = 'b_ sin_ s_ '
    other_word = 'business'
    if match_with_gaps(my_word, other_word) != False:
        print('FAILURE: test_match_with_gaps() when gussed letter appears less times in my word than it should')
        print('\t Expected True, but got ' + my_word)
    else: print('SUCCESS: test_match_with_gaps() when gussed letter appears less times in my word than it should')

    
if __name__ == "__main__":
    print("----------------------------------------------------------------------")
    test_get_guessed_word()
    print("----------------------------------------------------------------------")
    test_is_word_guessed()
    print("----------------------------------------------------------------------")
    test_get_available_letters()
    print("----------------------------------------------------------------------")
    test_match_with_gaps()
    print("----------------------------------------------------------------------")
