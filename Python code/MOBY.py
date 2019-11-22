def stringToWords(theLine):
    theList = ["--","!","?",",",".","\"",":",";"]
    
    # loop through the theList
    for i in theList:
        # replace the punction mark with a " "
        theLine = theLine.replace(i," ")
        
    return theLine



def main():

    theLine = input("type something bitch")
    theWords = stringToWords(theLine)
    print(theWords)

    return

main()
