def getYear(dateList):

    year = dateList[0]

    return year

def getMinTemp(dateList):

    minTemp = dateList[18]

    return float(minTemp)

def main():

    # Get the user's filename 1
    filename = input("what is your file's name: ")

    # Open the file 1
    inFile = open(filename,'r')

    # Initialze variables 2
    totalDays = 0
    freezingDays = 0

    # Read the column headers line 1
    coloumHeaders = inFile.readline()
    #print(coloumHeaders)
    # Read the first line of data 1
    line = inFile.readline()
    #print(line)
    # Read the newline character 1
    line = line.replace('\n','')
    #print(line)
    # Spilt the line ',' creating theList 1
    theList = line.split(',')
    #print(theList)
    # Create currentYear by calling getYear(theList) 1
    currentYear = getYear(theList)
    #print(currentYear)
    # Add one to totalDays 1
    totalDays += 1

    # If the temp is below freezing 1
    if (getMinTemp(theList) < 32):

        # Add one to the freeingDays 1
        freezingDays += 1

    #for each line in the input file 1
    for line in inFile:

        #remove the newline 1
        line = line.replace('\n','')

        #create a list using split(',') on the line 1
        theList = line.split(',')

        #check if what getYear(theList) gives you is different from currentYear 1
        if getYear(theList) != currentYear:

            #print out year and percentage (that is freezingDays divided by totalDays) 1
            print("the year {}, the percentage {}".format(getYear(theList),(float(freezingDays)/float(totalDays))))

            #zero out totalDays and freezingDays 2
            totalDays = 0
            freezingDays = 0

        #add one to totalDays 1
        totalDays += 1

        #If getMinTemp(theList) is below freezing 1
        if (getMinTemp(theList) < 32):

            #add one to freezingDays 1
            freezingDays += 1

        #set currentYear to getYear(theList) 1
        currentYear = getYear(theList)
        print(currentYear,(float(freezingDays)/float(totalDays)))
        
    #output the data from the last year in the file 1
    print("the days froozen last years was =",freezingDays) 

    return



main()
    
