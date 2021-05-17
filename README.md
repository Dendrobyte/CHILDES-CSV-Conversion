# CHILDES-CSV-Conversion

[![DOI](https://zenodo.org/badge/366402318.svg)](https://zenodo.org/badge/latestdoi/366402318)

A "small" script I wrote that converts CHILDES data into a spreadsheet format given certain forms of context.

**Context feature is broken, reach out if you want to use this and I can patch it real quick.**

## Information

This was written for a project I had for my First Language Acquisition class at NYU during the Spring 2021 semester. Professor is Ailis Cournane. My research project investigates child uses of "or" and whether children use "or" as an exclusive or ("xor") or and inclusive or ("ior"). I'll push my research paper to [my website](http://www.markobacon.com) when it's completed if you're curious.

## How It Works

The script is meant to be just that, and thus works in the shell, I didn't bother with UI or anything. The data will ask for a link to the `.cha` file on the [CHILDES database](https://sla.talkbank.org/TBB/childes/) and then prompt you for the search terms you intend to search of. A few more things that I intend to outline in this README once I finish the code, of course, and you'll end up with a CSV file with your data! You can also append data on to an existing spreadsheet if you'd like to compile data from multiple files.

## What It Looks Like

### Sample program run
![image](https://user-images.githubusercontent.com/12663558/117867560-86a06900-b266-11eb-8846-8e40a50e5262.png)

### Sample CSV (unfortunate about the blank lines, but alas)
![image](https://user-images.githubusercontent.com/12663558/117867625-9ae46600-b266-11eb-8f39-eb41701910df.png)

## Navigation

You can find all code files in the `Code` folder. The main script that should be run is `Main.py`, but uses the other files. Just maintains cleanliness of code.

You can find all exported CSVs, or put CSVs to modify, in the `Results` folder. If I revisit this project I might allow CSVs to be edited from other directories, but for now it is what it is. You can find a sample CSV in there right now, but otherwise the folder is gitignored. The program is not optimized by any means, so you must ensure you also have a `Downloaded` folder, just as in the release zip and the file structure of this repository. I did error catching where things showed up frequently, but when in doubt read the prompts!

Thanks for stopping by, and if you have any questions feel free to reach out via email or on Twitter, `@Mobkinz78` :D
