#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 11:06:54 2019

@author: DataScience 125
"""

from hangman import *

def test_is_word_guessed():

    Passed = True

    testCases = [
        ['m',           ['m'],                          True],
        ['m',           ['m', 'a', 'd'],                True],
        ['it',          ['i', 't'],                     True],
        ['it',          ['i', 't', 'k', 'f'],           True],
        ['apple',       ['a', 'p', 'l', 's'],           False],
        ['apple',       ['a', 'p', 'l', 'e'],           True],
        ['awkward',     ['a', 'w', 'k', 'r', 'd'],      True],
        ['banjo',       ['b', 'a', 'n', 'j', 'o'],      True],
        ['banjo',       ['b', 'a', 'k', 'p', 'r', 's'], False],
        ['fishhook',    ['f', 'i', 'h', 'k', 's'],      False],
        ['zzzz',        ['z', 'i'],                     True],
        ['zzzz',        ['z'],                          True],
        ['zzzz',        ['i'],                          False],
        ['zzzz',        ['d', 'i'],                     False],
    ]

    for case in testCases:
        secret_word = case[0]
        letters_guessed = case[1]
        expected_result = case[2]

        result = is_word_guessed(secret_word, letters_guessed)

        if result != expected_result:
            print("FAILURE: is_word_guessed()")
            print("\tExpected", str(expected_result) + ", but got", str(result),
                  "for secret_word: '" + secret_word + "' and letters_guessed:", letters_guessed)
            Passed = False

    if Passed:
        print("SUCCESS: is_word_guessed()")

def test_get_guessed_word():

    Passed = True

    testCases = [
        ['apple',           ['g'],                          '_ _ _ _ _ '],
        ['apple',           ['a'],                          'a_ _ _ _ '],
        ['apple',           ['a', 'p'],                     'app_ _ '],
        ['apple',           ['a', 'p', 'l'],                'appl_ '],
        ['apple',           ['a', 'p', 'l', 'e'],           'apple'],
        ['apple',           ['e', 'i', 'k', 'p', 'r', 's'], '_ pp_ e'],
        ['hood',            ['o'],                          '_ oo_ '],
        ['hood',            ['o', 'a', 'g'],                '_ oo_ '],
        ['hood',            ['o', 'a', 'd'],                '_ ood'],
        ['hood',            ['o', 'a', 'd','g', 'h'],       'hood'],
        ['tests',           [],       '_ _ _ _ _ '],
        ['tests',           ['t'],       't_ _ t_ '],
        ['tests',           ['t', 's'],       't_ sts'],
        ['moon',            ['n', 'm'],       'm_ _ n']
    ]

    for case in testCases:
        secret_word = case[0]
        letters_guessed = case[1]
        expected_result = case[2]

        result = get_guessed_word(secret_word, letters_guessed)

        if result != expected_result:
            print("FAILURE: is_word_guessed()")
            print("\tExpected", str(expected_result) + ", but got", str(result),
                  "for secret_word: '" + secret_word + "' and letters_guessed:", letters_guessed)
            Passed = False

    if Passed:
        print("SUCCESS: get_guessed_word()")

def test_get_available_letters():

    Passed = True

    testCases = [
        [[], 'abcdefghijklmnopqrstuvwxyz'],
        [['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'], ''],
        [['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'], 'a'],
        [['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y'], 'az'],
        [['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y'], 'amz'],
        [['a'], 'bcdefghijklmnopqrstuvwxyz'],
        [['z'], 'abcdefghijklmnopqrstuvwxy'],
        [['h', 'q'], 'abcdefgijklmnoprstuvwxyz'],
        [['a', 'm', 'n', 'z'], 'bcdefghijklopqrstuvwxy'],
        [['a', 'm', 'n', 'z', 'o'], 'bcdefghijklpqrstuvwxy'],
        [['e', 'i', 'k', 'p', 'r', 's'], 'abcdfghjlmnoqtuvwxyz'],
        [['c', 'b', 'a'], 'defghijklmnopqrstuvwxyz'], #out of order available letters
        [['a', 'b', 'a'], 'cdefghijklmnopqrstuvwxyz'] #repeated letters
    ]

    for case in testCases:
        letters_guessed = case[0]
        expected_result = case[1]

        result = get_available_letters(letters_guessed)

        if result != expected_result:
            print("FAILURE: is_word_guessed()")
            print("\tExpected", str(expected_result) + ", but got", str(result),
                  "with letters_guessed:", letters_guessed)
            Passed = False

    if Passed:
        print("SUCCESS: get_available_letters()")

print("----------------------------------------------------------------------")
print("Testing is_word_guessed...")
test_is_word_guessed()
print("----------------------------------------------------------------------")
print("Testing get_guessed_word...")
test_get_guessed_word()
print("----------------------------------------------------------------------")
print("Testing get_available_letters...")
test_get_available_letters()
print("----------------------------------------------------------------------")
