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
        if currLine[0] != "*CHI":
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
