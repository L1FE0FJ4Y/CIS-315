import sys
class coins():
    def __init__(self):
        self.coinsNum = 0
        self.maxUse = []
        self.coins = []

    def initialize(self, cNum, txt):
        self.coinsNum = cNum
        for i in range(1, self.coinsNum + 1):
            self.coins.append(int(txt[i].split()[0]))
            self.maxUse.append(0)

class MaxZordonCoin():
    def __init__(self):
        self.coinsList = None
        self.maxCoinsList = []
        self.targets = []
        self.targetsNum = 0

    def initialize(self, cList, tNum, txt):
        self.coinsList = cList
        self.targetsNum = tNum
        for i in range(self.coinsList.coinsNum + 1, self.coinsList.coinsNum + self.targetsNum + 1):
            self.targets.append(int(txt[i].split()[0]))

    def Launch(self):
        for i in range(self.targetsNum):
            self.calc(self.targets[i])
            self.maxCoinsList.append(self.maxCoins)

        for i in range(self.targetsNum):
            print("target: ", self.targets[i], end = ', ')
            if self.maxCoinsList[i] >= 0:
                print("max coins: ", self.maxCoinsList[i])
            else:
                print("not possible")

    def calc(self, target):
        coinCount = []
        maxUse = []
        CL = self.coinsList
        
        for i in range(target + 1):
            coinCount.append(-1)
            maxUse.append(-1)
        coinCount[0] = 0
        maxUse[0] = CL.maxUse.copy()

        for i in range(1,target + 1):
            for k in range(self.coinsList.coinsNum):
                j = CL.coinsNum - k - 1

                if (i - CL.coins[j]) >= 0:
                    if (coinCount[ i - CL.coins[j] ]) != -1:
                        if (maxUse[ i - CL.coins[j] ] [j]) < 5:
                            coinCount[i] = coinCount[ i - CL.coins[j] ] + 1
                            maxUse[i] = maxUse[ i - CL.coins[j] ].copy()
                            maxUse[i][j] += 1
                    
        self.maxCoins = coinCount[target]

def main():
    CL = coins()
    MZC = MaxZordonCoin()
    
    txtFile = sys.stdin.readlines()
    coinsNum, targetsNum = int(txtFile[0].split()[0]), int(txtFile[0].split()[1])
        
    CL.initialize(coinsNum, txtFile)
    MZC.initialize(CL, targetsNum, txtFile)
    MZC.Launch()


if __name__ == '__main__':
    main()
