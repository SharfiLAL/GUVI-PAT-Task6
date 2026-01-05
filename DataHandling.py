'''
Notepad = Login Credentials , config ., logs
CSV = Comma Separated Values
Excel = Test Data
Database = Live applicate


Notepad file


Plain Text
No Formatting
String
python reads it line by line


"Sharief \n" => meaning of \n end of the line, this is how Python reads it
"Gianna \n"
"Xenia \n"


1. Open the file
2. Read the data
3.Process the data
4.close the file


open("filename","mode")


r Read mode
w write mode
a Append mode


Problem statement
Read the file and give me the most repeated word











'''


file=open("dataDemo.txt","r")
data=file.read()
file.close()


print(data)


with open("dataDemo.txt","r") as file:
   for line in file:
       print(line.strip())
'''
with > auto closes the file
line > one line at a time
strip > removes spaces as well as in front of a line as in the back of a line \n


'''
