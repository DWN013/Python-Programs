#################################################
#      READ AutoDOX_README.txt BEFORE USE       #
#################################################
import sys
import os
lineBrk = "!!<!---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------->"
#Input filename that needs conversion, seperate extension from name
inName = sys.argv[1]
fileName, file_exten = os.path.splitext(inName)
#Deletes the last character ("_")
fileName = fileName[:-1]
outName = fileName + "_result.txt"
    
#with open('inFile.txt', 'r') as inFile, open('outFile.html', 'w') as outFile:
with open(inName, 'r') as inFile, open(outName, 'w') as outFile:
    outFile.write("!! Changes made before git 2018 and git version control can be found \\ref " + fileName + "_change_log \"here\" while changes after\n")
    outFile.write("!! this time can be found in git (logs and histories)\n!!\n!> \\file \n!> \page change_logs_pre_git Changelogs before 2018 (pre-git version control)\n")
    outFile.write("!! \n!!<table> \n!!<caption id=\"" + fileName + "_change_log\">Changelog for " + fileName + "</caption>\n")
    outFile.write(f"{lineBrk}\n!!<tr><th>Date</th>\t\t\t<th>User</th>\t\t\t\t<th><b>Comments</b></th>\n{lineBrk}\n")

    #Begin assembly of HTML table
    for line in inFile:
        #Iterate over  input file while splitting text between pipe into a list
        fields = line.split('|')

        #Split string into 3 sections, all text formatted on one line
        date = fields[0]
        names = fields[1]
        comments = fields[2]
        
        date = date.rstrip()
        date = date.lstrip().replace(" ", ". ")
        names = names.replace(".", ". ")
        ######################################################
        ## Error when encountering "::", treats it as a ": "
        ######################################################
        comments = comments.replace(": ", ":\t<br>\n")

        #Format fields for table
        formatted_date = f"<td>{date.strip().capitalize()}</td>\t\t"
        #Add break if there are multiple writers in names
        formatted_names = f"<td>{names.strip().title().replace('/', ' <br> ')}</td>\t\t\t"
        formatted_comments = "<td>"

        if("- " in comments):
            cmnt_list = comments.split("- ")
            #Format first comment independently
            formatted_comments += f"{cmnt_list[0].strip().capitalize()}<ul>"
            for i in range (1, len(cmnt_list)):
                # Split comments into individual sections and format
                formatted_comments += f"<li>{cmnt_list[i].strip().capitalize()}</li>"
            formatted_comments += "</ul>"
        else:
            formatted_comments += f"{comments.strip().capitalize()}"
        formatted_comments += "</td>"

        formatted_line = f"!!<tr>{formatted_date}{formatted_names}{formatted_comments}</tr>\n"
        outFile.write(f"{formatted_line}")
        outFile.write(lineBrk + "\n")
    outFile.write("!!</table>")
