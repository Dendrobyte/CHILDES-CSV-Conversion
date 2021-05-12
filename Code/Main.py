import wget
import os

import Utils as utils

while True:
    # Global variables
    savedFileName = ""

    # Begin
    print("-------------------------------------")
    print("Hello! Let's go ahead and turn that .cha into a nice manageable spreadsheet.")
    print(
        "CHILDES conversion to spreadsheet tool written by Mark Bacon -- @Dendrobyte on GitHub (Feel free to contribute!)")
    print("TO QUIT: When asked for link, enter 'q'")

    # Ask for the CHILDES file
    # TODO-FEAT: Input multiple files at once
    # TODO-FEAR: Skip this process if a file is already downloaded
    print(
        "Let's go ahead and start with the file you want to convert. Please copy the URL for the file (e.g. https://childes.talkbank.org/data-orig/Eng-NA/Brown/Adam/020304.cha)")

    # Change directory
    os.chdir(os.path.dirname(os.getcwd()))
    while True:

        reqURL = input("Link to TalkBank file: ")
        if(reqURL == 'q'):
            print("Bye!")
            exit()
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
        r = wget.download(reqURL, 'Downloaded/' + tbFileName)
        try:
            r = wget.download(reqURL, 'Downloaded/' + tbFileName)
        except:
            print("Hmm, something went wrong with the request. Here's the URL we tried: " + reqURL)
            print("Make sure you have a Downloaded folder!")
            continue
        else:
            savedFileName = tbFileName
            print("File downloaded!")
            break

    # Read in the CHILDES file and begin those relevant prompts
    print("Reading in the talkbank file...")

    # Attempt to open the file
    try:
        tbFile = open('Downloaded/' + savedFileName, 'r')
    except:
        print("Uhhh something went wrong with opening the file... Check the Downloaded folder?")
        break
    else:
        print("File read! Let's get started with the conversion, shall we?")

    # Read in file data
    tbFileData = tbFile.read()
    tbFileLines = tbFileData.split("\n")
    tbFile.close()

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

    # Check if there are lines with the utterance, and show them
    if len(resultLines.keys()) == 0:
        print("No results for that utterance, sorry!")
        break
    else:
        for line,contextlines in resultLines.items():
            print(line)
            print("--------")

    # Confirm whether they should add or append
    print("Time to save into a CSV file!")
    addOrAppend = input("Would you like to create a new file or append to an existing one? Enter C or A: ")
    create = True
    while True:
        if addOrAppend.lower() == "a" or addOrAppend.lower() == "c":
            break
        else:
            addOrAppend = input("That's not right... please enter 'C' for create or 'A' for append.")

    # Ensure name is valid
    while True:
        csvFileName = input("Please enter the name of the CSV file: ")

        # Check if file exists if it doesn't already
        if addOrAppend.lower() == "a":
            import os
            if (csvFileName + ".csv") in os.listdir('Results'):
                create = False
                break
            else:
                print("Hmm, that file doesn't exist. Make sure it's in the Results folder and is a .csv file")
                if('.' in csvFileName):
                    print("Also, don't add an extension. Just write the file's name! I assume it's a CSV.")
        else:
            break
        """elif addOrAppend.lower == "c":
            import os

            if (csvFileName + ".csv") in os.listdir('Results'):
                create = False
                print("That file already exists! Try a different name.")"""

    # Handle file opening for writing
    # TODO-FEAT: You see why I should be able to skip straight to here? Haha
    csvFileName = 'Results/' + csvFileName + ".csv"

    # Write the data to the file
    success = utils.writeToCSV(csvFileName, resultLines, create, savedFileName)

    # Clean up blank rows of the file


    # Finish it up
    if success:
        print("Mission accomplished!")
        print("Your file can be found in " + csvFileName)
    else:
        print("Something went wrong, sorry!")

