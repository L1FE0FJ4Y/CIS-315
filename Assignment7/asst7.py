"""
Jay Shin Assignment7
Recursive Memo Version
"""
class WBR:
    def wordBreak(self, string, wordDict):
        res = []
        memo = dict()
        return self.recursion(string, res, wordDict, memo)
    
    def recursion(self, string, res, wordDict, memo):
        #if string is everything then
        if string in memo:
            return memo[string]
        #Nothing in string
        if not string:
            return [""]

        res = []
        for word in wordDict:
            #check adding up next char to check the word
            if string[:len(word)] != word: continue
            if len(res) < 1:
            #if we get word then recursion the right side of word in string
                for recursionString in self.recursion(string[len(word):], res, wordDict, memo):
                    if not recursionString:
                        res.append(word + "")
                    else:
                        res.append(word + " " + recursionString)
        #memo the string so we can use later 
        memo[string] = res
        return res

def main():
    Dict = {}
    fp = open("diction10k.txt", "r")
    for string in fp:
        Dict[string[:len(string)-1]] = True

    res = WBR()

    inputS = input()
    for i in range(int(inputS)):
        string = input()
        print("Phrase Number: ", i + 1)
        print(string)
        if(res.wordBreak(string, Dict)):
            print(res.wordBreak(string, Dict)[0])
            print()
        else:
            print()

    fp.close()
    
if __name__ == "__main__":
    main()
    


