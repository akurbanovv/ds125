from hangman import *

# Problem Set 3, test_hangman.py
# Name: Akhmadjon Kurbanov
# Collaborators:
# Time spent:

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
    else: print('SUCCESS: test_get_guessed_word() with all letters guessed')

def test_get_available_letters():
    print('Testing test_get_available_letters()\n')

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


if __name__ == "__main__":
    print("----------------------------------------------------------------------")
    test_get_guessed_word()
    print("----------------------------------------------------------------------")
    test_is_word_guessed()
    print("----------------------------------------------------------------------")
    test_get_available_letters()
    print("----------------------------------------------------------------------")



    