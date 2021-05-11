import csv

# This is the file that does all the actual converting stuff, helps keep things clean.

"""
utterance -- Utterance being looked for
filedatalines -- File data that has been opened and split by newline character
contextNum -- Number of lines of context to find
returns linesDict -- Dictionary where the keys are the lines and the values are a list of context lines
"""
def findLines(utterance, filedatalines, contextNum):
    # TODO-FEAT: Implement this to work with more than just child utterances
    # Initialize dictionary
    linesDict = {}
    # Keep track of line number without using index function
    lineNumber = 0
    # Go ahead and check each line
    for line in filedatalines:
        # Split line by space
        currLine = line.split(" ")
        # Skip if it's not a child utterance
        if currLine[0][0:4] != "*CHI":
            continue
        # Search for utterance
        if utterance.lower() in currLine:
            # Put utterance into the dictionary with an empty list
            linesDict[line] = []
            if contextNum != 0:
                linesDict[line] = findContext(lineNumber, contextNum)
        lineNumber += 1
    return linesDict

"""
lineNumber -- The line number to check
contextNum -- Number of lines to get before and after a given line
returns contextLines -- A list of lines of context, where a "|" separates pre and post context
"""


def findContext(lineNumber, contextNum):
    return ["pre-test", "|", "post-test"]
"""
csvFileName -- File name for the csv file to open and write to
resultLines -- The lines we write to the csv file
create -- Whether or not the file is being created or appended to
fileName -- Name of the file

returns boolean -- True if success, False if not
"""
def writeToCSV(csvFileName, resultLines, create, fileName):
    try:
        # TODO: Figure out new line issue
        csvFile = open(csvFileName, 'a+')
    except:
        print("Oof, something happened with trying to open the CSV file.")
        return False

    # Initialize CSV writer
    print("Now writing lines into " + csvFileName + "...")
    csvWriter = csv.writer(csvFile)

    # Create the first row with labels if it's a new file
    if create:
        csvWriter.writerow(['Corpus', 'Child Name', 'File Name', 'Main Line Utterance', 'Pre-Context', 'Post-Context'])

    # Grab the respective info from the fileName passed into the function
    corpus = fileName.split("-")[0]
    childName = fileName.split("-")[1]
    fileName = fileName.split("-")[2]

    # Write all the lines
    for line,context in resultLines.items():
        # Get the context
        if len(context) != 0:
            midOfContext = context.index("|")
            preContext = context[0:midOfContext]
            postContext = context[midOfContext+1::]

            # Write the row with context
            csvWriter.writerow([corpus, childName, fileName, line, preContext, postContext])
        else:
            # Write the row without context
            csvWriter.writerow([corpus, childName, fileName, line, 'no context', 'no context'])

    # Close the file
    csvFile.close()
    return True