# Assigment: CoinFlips
# Name: Akhmadjon Kurbanov

import random

# by flipping the coin get H (heads) or T (tails)
def flipCoin():
    return random.choice(['T','H'])

# Return true of flips result has at least two heads, otherwise false
def gotMatch(n):
    counter = 0
    for i in range(n):
        if flipCoin() == 'H':
            counter += 1 
            if counter >= 2: return True
    return False

# calculate probability empirically
def empirProb(n, numTrials):
    numHits = 0
    for i in range(numTrials):
        if gotMatch(n):
            numHits += 1
    return numHits/numTrials

# calculate probability theoretically
def theorProb(n):
    return 1 - ((1+ n)/(2**n))

if __name__ == '__main__':
    numTrials = 10000
    numFlips = [2, 3, 4, 5, 10, 20, 100]
    for n in numFlips:
        print('For N =', n)
        print('The Theoretical Probability:', round(theorProb(n), 4))
        print('The Empirical Probability:  ', round(empirProb(n, numTrials), 4))
        print()
