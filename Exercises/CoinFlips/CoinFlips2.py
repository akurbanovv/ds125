# Assigment: CoinFlips pt2
# Name: Akhmadjon Kurbanov

import random
import matplotlib.pyplot as plt

# by flipping the coin get H (heads) or T (tails)
def flipCoin():
    return random.choice(['T','H'])

# Return true of flips result has at least two heads, otherwise false
def gotMatch(n, k):
    result = ''
    for i in range(n):
        result += flipCoin()
    if result.count('H') == k: return True
    return False

# calculate probability empirically
def empirProb(n, numTrials, k):
    numHits = 0
    for i in range(numTrials):
        if gotMatch(n, k):
            numHits += 1
    return numHits/numTrials

# calculate probability theoretically
def theorProb(n):
    return 1 - ((1+ n)/(2**n))

# draw a histogram
def drawGraph(kList, probList):
    probList = [i * 100 for i in probList]
    plt.bar(kList, probList)
    plt.xticks(kList)
    plt.title('Probability for getting k heads per ' + str(numFlips)
    + ' flips after ' + str(numTrials) + ' trials')
    plt.ylabel('Probability (%)')
    plt.xlabel('Number of heads (k)')
    plt.show()

if __name__ == '__main__':
    numTrials = 10000
    numFlips = 10
    kList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    probList = []

    for k in kList:
        probList.append(round(empirProb(numFlips, numTrials, k), 4))

    print(sum(probList))
    drawGraph(kList, probList)


