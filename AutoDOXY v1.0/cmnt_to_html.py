#################################################
#      READ AutoDOX_README.txt BEFORE USE       #
#################################################
import sys
import os
#Pre-defined string so there doesn't need to be a massive line in script constantly
lineBrk = "!!<!---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------->"

#Input filename that needs conversion, seperate extension from name
inName = sys.argv[1]
fileName, file_exten = os.path.splitext(inName)

#Output file result
outName = fileName + "_result.txt"
    
#with open('inFile.txt', 'r') as inFile, open('outFile.html', 'w') as outFile:
with open(inName, 'r') as inFile, open(outName, 'w') as outFile:
    outFile.write("!! Changes made before git 2018 and git version control can be found \\ref " + fileName + "_change_log \"here\" while changes after\n")
    outFile.write("!! this time can be found in git (logs and histories)\n!!\n!> \\file \n!> \page change_logs_pre_git Changelogs before 2018 (pre-git version control)\n")
    outFile.write("!! \n!!<table> \n!!<caption id=\"" + fileName + "_change_log\">Changelog for " + fileName + "</caption>\n")
    outFile.write(f"{lineBrk}\n!!<tr><th>Date</th>\t\t\t<th>User</th>\t\t\t\t<th><b>Comments</b></th>\n{lineBrk}\n")
    #Begind assembly of HTML table
    for line in inFile:
        #Iterate over  input file while splitting text between pipe into a list
        fields = line.split('|')
        #Split string into 3 sections, all text formatted on one line
        date = fields[0]
        names = fields[1]
        comments = fields[2]
        #Add break if there are multiple writers in names
        date = date.rstrip()
        date = date.replace(" ", ". ")
        names = names.replace("/", " <br> ")
        comments = comments.replace(":", ":\t<br>\n")
        #Format fields for table
        formatted_date = f"<td>{date.strip().capitalize()}</td>\t"
        formatted_names = f"<td>{names.strip().capitalize()}</td>\t"
        formatted_comments = "<td>"
        if('-' in comments):
            for comment_list in comments.split('-'):
                # Split comments into individual sections and format
                formatted_comments += f"<li>{comment_list.strip().capitalize()}</li>"
        else:
            formatted_comments += f"{comment_list.strip().capitalize()}"
        formatted_comments += "</td>"
        formatted_line = f"!!<tr>{formatted_date}{formatted_names}{formatted_comments}</tr>\n"
        outFile.write(f"{formatted_line}")
        outFile.write(lineBrk + "\n")
        #Output formatted data to _result.txt
    outFile.write("!!</table>")
