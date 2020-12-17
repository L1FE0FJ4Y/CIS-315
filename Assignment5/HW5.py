import sys
class coins():
    def __init__(self):
        self.numCoins = 0
        self.coinsAvailable = []
        self.coinsList = []

    def initializeCoins(self, numC, startLine):
        self.numCoins = numC
        for i in range(1, self.numCoins + 1):
            if startLine[i].split()[0].isdigit():
                self.coinsList.append(int(startLine[i].split()[0]))
                self.coinsAvailable.append(5)
                ret = True
            else:
                print("coins:initializeCoins() Failed!")
                print("Line ", i + 1, " is not a number!")
                self.coinsList = []
                ret = False
                break
        return ret

    def resetCoinsAvailable(self):
        for i in range(self.numCoins):
            self.coinsAvailable[i] = 5

class MaxZordonCoin():
    def __init__(self):
        self.coinsSet = None
        self.maxCoinsList = []
        self.targetList = []
        self.numTargets = 0

    def initializeMZC(self, coinsL, numT, startLine):
        self.coinsSet = coinsL
        self.numTargets = numT
        for i in range(self.coinsSet.numCoins + 1, self.coinsSet.numCoins + self.numTargets + 1):
            if startLine[i].split()[0].isdigit():
                self.targetList.append(int(startLine[i].split()[0]))
                ret = True
            else:
                print("MaxZordonCoin:initializeMZC() Failed!")
                print("Line ", i + 1, " is not a number!")
                self.targetList = []
                ret = False
                break
        return ret

    def calcMZC(self):
        for i in range(self.numTargets):
            self.calculate(self.targetList[i])
            self.maxCoinsList.append(self.maxCoins)
            self.maxCoins = -1
            self.coinsSet.resetCoinsAvailable()

    def calculate(self, target):
        table = []
        useTable = []
        for i in range(target + 1):
            table.append(-1)
            useTable.append(-1)
        for i in range(target + 1):
            for k in range(self.coinsSet.numCoins):
                j = self.coinsSet.numCoins - k - 1
                if i == 0:
                    table[i] = 0
                    useTable[i] = self.coinsSet.coinsAvailable.copy()
                elif i - self.coinsSet.coinsList[j] >= 0 and table[i - self.coinsSet.coinsList[j]] != -1 and useTable[i - self.coinsSet.coinsList[j]][j] > 0:
                    table[i] = table[i - self.coinsSet.coinsList[j]] + 1
                    useTable[i] = useTable[i - self.coinsSet.coinsList[j]].copy()
                    useTable[i][j] -= 1
        self.maxCoins = table[target]

    def printMZC(self):
        for i in range(self.numTargets):
            print("target: ", self.targetList[i], end = '')
            if self.maxCoinsList[i] >= 0:
                print(", max coins: ", self.maxCoinsList[i])
            else:
                print(", not possible")


def main():
    coinsSet = coins()
    mzc = MaxZordonCoin()
    f = sys.stdin
    f1 = f.readlines()
    if f1[0].split()[0].isdigit() and f1[0].split()[1].isdigit():
        numCoin, numTarget = int(f1[0].split()[0]), int(f1[0].split()[1])
        iniCoinStatus = coinsSet.initializeCoins(numCoin, f1)
        iniMZCStatus = mzc.initializeMZC(coinsSet, numTarget, f1)
        if iniCoinStatus and iniMZCStatus:
            mzc.calcMZC()
            mzc.printMZC()
    else:
        print("The first line is not numbers!")

if __name__ == '__main__':
    main()
