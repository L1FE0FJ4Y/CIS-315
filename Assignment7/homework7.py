"""
CIS 315: Intermediate Algorithms
Dynamic Programming: Splitting Strings
Author: Jarett Nishijo
"""

def in_dict(word, dic):
    if word in dic:
        return True
    return False

def reconstruct(splitloc, s):
    ret = ""
    iteration = 0
    first = False

    for i in range(1,len(s)):
        if iteration < i:
            iteration = i
        if splitloc[iteration] != 0:

            if first == False:
                ret += s[:i] + " "
                first = True
            if iteration >= len(s)-1:
                ret += s[iteration:]
                break
            else:
                next_word = s[iteration:splitloc[iteration]]
                ret += next_word + " "
                iteration = splitloc[iteration]
    return ret

def split_iter(s, dic):

    DPtable = []    #Init DP table and split location array
    splitloc = []

    if s == "":     #Base Case
        return True, DPtable

    for i in range(len(s) + 1): #fill DP table and split locations with values
        DPtable.append(False)
        splitloc.append(0)

    for i in range(1, len(s)+1):
        if DPtable[i] == False and in_dict(s[0:i],dic): #first valid word of string. Try for every possible word after
            splitloc[0] = i
            DPtable[i] = True

        if DPtable[i] == True:                          #String is 1 valid word
            if i == len(s):
                return True,splitloc

            for j in range(i+1, len(s)+1):              #Trying all other words after first

                if DPtable[j] == False and in_dict(s[i:j],dic): #Fill DP Table and location of word
                    splitloc[i] = j
                    DPtable[j] = True

                if j == len(s) and DPtable[j] == True:  #Found a splittable string
                    return True,splitloc

    return False, splitloc

def main():
    dic = {}
    fp = open("diction10k.txt", "r")
    for x in fp:
        dic[x[:len(x)-1]] = True    #Fill dictionary with words

    C = input()
    for i in range(int(C)):
        x = input()
        print("Phrase Number: ", i + 1)
        print(x)
        y = split_iter(x, dic)
        if (y[0] == True):
            str = reconstruct(y[1],x)
            print("Iterative attempt")
            print("YES, can be split")
            print(str)
            print()
        else:
            print("NO, cannot be split")
            print()

    fp.close()

if __name__ == "__main__":
    main()
