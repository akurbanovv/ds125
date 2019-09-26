#
# Assigment: CoinFlips
# Name: Akhmadjon Kurbanov
#

import random


def flipCoin():
    #1 is heads, 0 is tails
    return random.choice(['T','H'])

def gotMatch(n, targetMatch):
    result = ''
    for i in range(n):
        result += flipCoin()
    if targetMatch in result: return True
    else: return False

def matchProb(n, numTrials):
    numHits = 0
    targetMatch = 'HH'
    for i in range(numTrials):
        if gotMatch(n, targetMatch):
            numHits += 1
    return numHits/numTrials
    
if __name__ == '__main__':
    





        





