import csv
import wget

import Utils as utils

# Global variables
savedFileName = ""

# Begin

print("Hello! Let's go ahead and turn that .cha into a nice manageable spreadsheet.")
print(
    "CHILDES conversion to spreadsheet tool written by Mark Bacon -- @Dendrobyte on GitHub (Feel free to contribute!)")

# Ask for the CHILDES file
# TODO-FEAT: Input multiple files at once
# TODO-FEAR: Skip this process if a file is already downloaded
print(
    "Let's go ahead and start with the file you want to convert. Please copy the URL for the file (e.g. https://childes.talkbank.org/data-orig/Eng-NA/Brown/Adam/020304.cha)")

while True:

    reqURL = input("Link to TalkBank file: ")

    # Split up the URL for validation
    splitURL = reqURL.split("/")

    # Make sure it's a talkbank link
    if "childes.talkbank.org" not in splitURL:
        print("Invalid link! Link should start with \'childes.talkbank.org\'.")
        if "sla.talkbank.org" in splitURL:
            print("Looks like you pasted in \'sla.talkbank.org\'. Make sure to click on the transcript hyperlink at "
                  "the top of the page under \'CHAT\'.")
        continue

    # Create a "unique" filename
    tbFileName = splitURL[-3] + "-" + splitURL[-2] + "-" + splitURL[-1]

    # Download the file to the Downloaded folder
    print("Attempting to import {} from the provided URL...".format(splitURL[-1]))
    try:
        r = wget.download(reqURL, '../Downloaded/' + tbFileName)
    except:
        print("Hmm, something went wrong with the request. Here's the URL we tried: " + reqURL)
        continue
    else:
        savedFileName = tbFileName
        print("File downloaded!")
        break

# Read in the CHILDES file and begin those relevant prompts
print("Reading in the talkbank file...")

# Attempt to open the file
try:
    tbFile = open('../Downloaded/' + 'savedFileName')
except:
    print("Uhhh something went wrong with opening the file... Check the Downloaded folder?")
    exit()
else:
    print("File read! Let's get started with the conversion, shall we?")

# Read in file data
tbFileData = tbFile.read()
tbFileLines = tbFileData.split("\n")

# Ask for search term and whatnot
print("What is the word/utterance you are searching for?")
print("Please Note: This program will only look at child utterances, marked as CHI in the file.")
utterance = input("Search term / utterance: ")

# Ask for context
print("How many lines of context would you like? Returns \'n\' lines before and after the utterance. Enter 0 for no "
      "context.")
# Validate lines of context
while True:
    context = input("Please enter a number of context lines: ")
    try:
        context = int(context)
    except:
        print("Please enter a whole number, no decimals.")
        continue
    else:
        break

# Print a sample
print("Alrighty... let's find what you need, shall we? How does this look?")

resultLines = utils.findLines(utterance, tbFileLines, context)

for line,contextlines in resultLines.items():
    print(line)
    print("\n--------\n")
