# Assigment: CoinFlips pt2
# Name: Akhmadjon Kurbanov

import random
import math
import matplotlib.pyplot as plt
import statistics

# by flipping the coin get H (heads) or T (tails)
def flipCoin():
    return random.choice(['T','H'])

# Return true of flips result has excaty K heads, otherwise false
def gotMatch(numFlips, k):
    result = ''
    for i in range(numFlips):
        result += flipCoin()
    if result.count('H') == k: return True
    return False

sampleMeansList = []
# calculate probability by running simulation 
def calcProb(numFlips, k, numSamples, sampleSize):
    sampleMeans = []
    for i in range(numSamples):
        numHits = 0
        for j in range(sampleSize):
            if gotMatch(numFlips, k):
                numHits += 1
        sampleMean = numHits/sampleSize
        sampleMeans.append(sampleMean)
    
    sampleMeansList.append(sampleMeans)
    return round(calcMean(sampleMeans), 4)

def calcMean(probList):
    mean = statistics.mean(probList)
    return mean

def calcSTD(probList):
    std = statistics.stdev(probList)                          
    return std

def calc95CI(probList):
    std = calcSTD(probList)      
    n = len(probList)                  
    SEM = std / math.sqrt(n)

    mean = calcMean(probList)     
    width = round(1.96*SEM, 2)

    return (mean, width)


# draw a histogram
def drawGraph(kList, probList, meansList, ciList):
    # probList = [i * 100 for i in probList]
    plt.bar(kList, probList)
    plt.errorbar(kList, meansList, xerr = 0.3, yerr=ciList, linewidth=1, color='red')
    plt.plot(kList, meansList)

    plt.xticks(kList)
    plt.title('Probability for getting k heads per ' + str(numFlips)
    + ' flips \n with the number of samples - ' + str(numSamples) 
    + ', and sample size - ' + str(sampleSize) + '.')
    plt.ylabel('Probability (%)')
    plt.xlabel('Number of heads (k)')
    plt.show()

if __name__ == '__main__':
    numFlips = 10
    numSamples = 100
    sampleSize = 100

    kList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    probList = []
    meansList = []
    ciList = []

    ci = ()

    # run simulation for k and get probability  
    for k in kList:
        probList.append(calcProb(numFlips, k, numSamples, sampleSize))
        ci = calc95CI(sampleMeansList[k])
        meansList.append(ci[0])
        ciList.append(ci[1])

    drawGraph(kList, probList, meansList, ciList)


