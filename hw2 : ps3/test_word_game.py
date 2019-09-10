from ps3 import *
#import ps3
#
# Test code for the word game problem, refactored to make smaller, more
# clearly defined unit tests
#

PASSED = True
FAILED = not PASSED

def test_get_word_score(words, words_type):
    """
    Prints the test result for the given words dictionary and words_type.

    tests get_word_score with the given words dictionary
    and a string description of the words_type, and prints
    FAILURE or SUCCESS based on the test results, including
    information of the failed test cases.

    words: dictionary ((word, n) -> expected score)
    words_type: string, describing the type of words in the dictionary
    """

    failure=False
    for (word, n) in words.keys():
        score = get_word_score(word, n)
        if score != words[(word, n)]:
            print("FAILURE: test_get_word_score() with", words_type)
            print("\tExpected", words[(word, n)], "points but got '" + \
                  str(score) + "' for word '" + word + "', n=" + str(n))
            failure=True

    if not failure:
        print("SUCCESS: test_get_word_score() with", words_type)

def test_get_word_score_all():
    """
    Unit test for get_word_score
    """

    # dictionary of words and scores
    words_empty = {("", 0):0, ("", 1):0, ("", 7):0}
    words_in_lowercase = {("it", 7):2, ("was", 7):54, ("weed", 6):176,
                          ("scored", 7):351, ("fork", 7):209}
    words_in_mixedcases = { ("WaYbILl", 7):735, ("Outgnaw", 7):539,
              ("FORK", 4):308}

    test_get_word_score(words_empty, "empty words")
    test_get_word_score(words_in_lowercase, "words in lowercase")
    test_get_word_score(words_in_mixedcases, "words having uppercase letters")



# end of test_get_word_score


def test_update_hand(handOrig, word, expected_hand1, expected_hand2, test_info):

    handCopy = handOrig.copy()

    hand2 = update_hand(handCopy, word)
    if hand2 != expected_hand1 and hand2 != expected_hand2:
        print("FAILURE: test_update_hand with")
        print("\t" + test_info + ", specifically:")
        print("\t(" + str(handOrig) +", '" + word + "')")
        print("\tReturned: ", hand2, "\n\t-- but expected:",
              expected_hand1, "or\n\t\t", expected_hand2, "\n")

        return FAILED  # exit function

    if handCopy != handOrig:
        print("FAILURE: test_update_hand with")
        print("\t" + test_info + ", specifically:")
        print("\t(" + str(handOrig) +", '" + word + "')")
        print("\tOriginal hand was", handOrig)
        print("\tbut implementation of update_hand mutated the original hand!")
        print("\tNow the hand looks like this:", handCopy, "\n")

        return FAILED # exit function

    print("SUCCESS: test_update_hand() with", test_info)
    return PASSED

def test_update_hand_all():
    """
    Unit test for update_hand. What cases get tested? What other cases should
    be tested and what are their expected results?
    """
    all_passed = True
    # test 1
    handOrig = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
    word = "quail"
    expected_hand1 = {'l':1, 'm':1}
    expected_hand2 = {'a':0, 'q':0, 'l':1, 'm':1, 'u':0, 'i':0}

    test_passed = test_update_hand(handOrig, word, expected_hand1, expected_hand2,
                     "a lowercase word in the hand")
    all_passed = all_passed and test_passed

    # test 2
    handOrig = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
    word = "Evil"
    expected_hand1 = {'v':1, 'n':1, 'l':1}
    expected_hand2 = {'e':0, 'v':1, 'n':1, 'i':0, 'l':1}
    test_passed = test_update_hand(handOrig, word, expected_hand1, expected_hand2,
                     "a mixedcase word in the hand")
    all_passed = all_passed and test_passed

    # test 3
    handOrig = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    word = "HELLO"
    expected_hand1 = {}
    expected_hand2 = {'h': 0, 'e': 0, 'l': 0, 'o': 0}
    test_passed = test_update_hand(handOrig, word, expected_hand1, expected_hand2,
                     "an uppercase word in the hand, "
                     + "resulting in an empty updated hand\n")
    all_passed = all_passed and test_passed


    word = "HELLO0"
    test_passed = test_update_hand(handOrig, word, expected_hand1, expected_hand2,
            "a word not in the hand \n"
            + "\tdue to a number, resulting in an empty updated hand\n")
    all_passed = all_passed and test_passed

    word = "HELLOooo"
    test_passed = test_update_hand(handOrig, word, expected_hand1, expected_hand2,
            "a word not in the hand \n"
            +"\tdue to a letter requested too many times\n")
    all_passed = all_passed and test_passed

    if(all_passed):
        print("SUCCESS: test_update_hand()")

# end of test_update_hand

def test_is_valid_word(word_list):
    """
    Unit test for is_valid_word
    """
    failure=False
    # test 1
    word = "hello"
    handOrig = get_frequency_dict(word)
    handCopy = handOrig.copy()

    if not is_valid_word(word, handCopy, word_list):
        print("FAILURE: test_is_valid_word()")
        print("\tExpected True, but got False for word: '" + word + "' and hand:", handOrig)

        failure = True

    # Test a second time to see if word_list or hand has been modified
    if not is_valid_word(word, handCopy, word_list):
        print("FAILURE: test_is_valid_word()")

        if handCopy != handOrig:
            print("\tTesting word", word, "for a second time - be sure you're not modifying hand.")
            print("\tAt this point, hand ought to be", handOrig, "but it is", handCopy)

        else:
            print("\tTesting word", word, "for a second time - have you modified word_list?")
            wordInWL = word in word_list
            print("The word", word, "should be in word_list - is it?", wordInWL)

        print("\tExpected True, but got False for word: '" + word + "' and hand:", handCopy)

        failure = True


    # test 2
    hand = {'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u':1}
    word = "Rapture"

    if  is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word()")
        print("\tExpected False, but got True for word: '" + word + "' and hand:", hand)

        failure = True

    # test 3
    hand = {'n': 1, 'h': 1, 'o': 1, 'y': 1, 'd':1, 'w':1, 'e': 2}
    word = "honey"

    if  not is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word()")
        print("\tExpected True, but got False for word: '"+ word +"' and hand:", hand)

        failure = True

    # test 4
    hand = {'r': 1, 'a': 3, 'p': 2, 't': 1, 'u':2}
    word = "honey"

    if  is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word()")
        print("\tExpected False, but got True for word: '" + word + "' and hand:", hand)

        failure = True

    # test 5
    hand = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
    word = "EVIL"

    if  not is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word()")
        print("\tExpected True, but got False for word: '" + word + "' and hand:", hand)

        failure = True

    # test 6
    word = "Even"

    if  is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word()")
        print("\tExpected False, but got True for word: '" + word + "' and hand:", hand)
        print("\t(If this is the only failure, make sure is_valid_word() isn't mutating its inputs)")

        failure = True

    # test by Akhmad Kurbanov
    word = "m*lk"
    hand = {'m':1, 'i':2, 'l':1, 'k':1, 'g':1}

    if is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word() with a word with asterisk but hand does not have one")
        print("\tExpected False, but got True for word: '" + word + "' and hand:", hand)
        failure = True

    if not failure:
        print("SUCCESS: test_is_valid_word()")






# end of test_is_valid_word

def test_wildcard(word_list):
    """
    Unit test for is_valid_word
    """
    failure=False

    # test 1
    hand = {'a': 1, 'r': 1, 'e': 1, 'j': 2, 'm': 1, '*': 1}
    word = "e*m"

    if is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word() with wildcards")
        print("\tExpected False, but got True for word: '" + word + "' and hand:", hand)

        failure = True

    # test 2
    hand = {'n': 1, 'h': 1, '*': 1, 'y': 1, 'd':1, 'w':1, 'e': 2}
    word = "honey"

    if is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word() with wildcards")
        print("\tExpected False, but got True for word: '"+ word +"' and hand:", hand)

        failure = True

    # test 3
    hand = {'n': 1, 'h': 1, '*': 1, 'y': 1, 'd':1, 'w':1, 'e': 2}
    word = "h*ney"

    if not is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word() with wildcards")
        print("\tExpected True, but got False for word: '"+ word +"' and hand:", hand)

        failure = True

    # test 4
    hand = {'c': 1, 'o': 1, '*': 1, 'w': 1, 's':1, 'z':1, 'y': 2}
    word = "c*wz"

    if is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word() with wildcards")
        print("\tExpected False, but got True for word: '"+ word +"' and hand:", hand)

        failure = True

    # test 5
    hand = {'c': 1, 'o': 1, '*': 1, 'm': 1, 'n': 2}
    word = "m**n"

    if is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word() with wildcards")
        print("\tExpected False, but got True for word: '"+ word +"' and hand:", hand)

        failure = True

    # dictionary of words and scores WITH wildcards
    words = {("h*ney", 7):290, ("c*ws", 6):176, ("wa*ls", 7):203}
    for (word, n) in words.keys():
        score = get_word_score(word, n)
        if score != words[(word, n)]:
            print("FAILURE: test_get_word_score() with wildcards")
            print("\tExpected", words[(word, n)], "points but got '" + \
                  str(score) + "' for word '" + word + "', n=" + str(n))
            failure=True

    if not failure:
        print("SUCCESS: test_wildcard()")


word_list = load_words()
print("----------------------------------------------------------------------")
print("Testing get_word_score...")
test_get_word_score_all()
print("----------------------------------------------------------------------")
print("Testing update_hand...")
test_update_hand_all()
print("----------------------------------------------------------------------")
print("Testing is_valid_word...")
test_is_valid_word(word_list)
print("----------------------------------------------------------------------")
print("Testing wildcards...")
test_wildcard(word_list)
print("----------------------------------------------------------------------")
print("All done!")
