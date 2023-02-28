#################################################
#      READ AutoDOX_README.txt BEFORE USE       #
#################################################
import sys
import os
#import cmnt_to_html

#Input filename that needs conversion, seperate extension from name
inName = sys.argv[1]
fileName, file_exten = os.path.splitext(inName)

#Output file result
outName = fileName + "_final"

with open(inName, 'r') as inFile, open(outName, 'w') as outFile:
    for line in inFile:
        outFile.write(line[10:])
    inFile.close()
    outFile.close()

#os.system(f"python3 cmnt_to_html.py, {outName}")
