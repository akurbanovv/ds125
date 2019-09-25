#
# Assigment: CoinFlips
# Name: Akhmadjon Kurbanov
#

import random


def flipCoin():
    #1 is heads, 0 is tails
    return random.choice([1,0])

def testRoll(n = 10):
    result = '' 
    for i in range(n):
        result = result + str(flipCoin()) 
    print(result)

def runSim(goal, numTrials, txt):
    total = 0

if __name__ == '__main__':
    testRoll(2)
    





        





