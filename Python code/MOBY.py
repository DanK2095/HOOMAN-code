
def stringToWords(theLine):
    theList = ["--","!","?",",",".","\"",":",";","  "]
    
    # loop through the theList
    for i in theList:

        if i == '\"':
            theLine = theLine.replace(i,"")
        else: 
            # replace the punction mark with a " "
            theLine = theLine.replace(i," ")
            
    stringList = theLine.lower().split(' ')
    
    return stringList

def processWords(wordList,theDict):
    
    for currentWord in wordList:

        if currentWord in theDict:
            theDict[currentWord] = theDict[currentWord] + 1
        else:
            theDict[currentWord] = 1
            
    return theDict

def ByFreq(pair):
    return pair[1]

def main():

    fileName = input("What is the name of your file?: ")
    
    file = open(fileName,'r')

    theDict = {}
    
    for line in file:
        
        line = line.replace('\n',' ')
        wordList = stringToWords(line)
        theDict = processWords(wordList,theDict)
    
    dictList = list(theDict.items())
    dictList.sort()
    dictList.sort(key = ByFreq, reverse = True)
    for i in dictList:
        print(i)
        
    return

main()
