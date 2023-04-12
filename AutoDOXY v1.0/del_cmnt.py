#################################################
#      READ AutoDOX_README.txt BEFORE USE       #
#################################################
import sys
import os
#Input filename that needs conversion, seperate extension (.xyz) from name
inName = sys.argv[1]
fileName, file_exten = os.path.splitext(inName)

#Output filename
outName = fileName + "_"

with open(inName, 'r') as inFile, open(outName, 'w') as outFile:
    for line in inFile:
        formatted_cmnt = line.lstrip()
        formatted_cmnt = formatted_cmnt[1:].lstrip()
        if(formatted_cmnt[0:1] == '*'):
            formatted_cmnt = formatted_cmnt[1:]
        outFile.write(formatted_cmnt)
    inFile.close()
    outFile.close()
#os.system(f"python3 cmnt_to_html.py, {outName}")
