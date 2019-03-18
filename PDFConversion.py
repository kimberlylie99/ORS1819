import PyPDF2
import fileinput
from tika import parser


newfile = open("TheHelpConversion.txt","wb")
#file = open("TheHelp.pdf","r")

raw = parser.from_file("theHelp.pdf");
test = raw['content']
print(test);
test = test.encode('utf-8')
newfile.write(test);
#file.close();
newfile.close();


#newfile = open("TheHelpConversion.txt","wb")
#file = open("TheHelp.pdf","rb")
#pdfreader = PyPDF2.PdfFileReader(file)
#index = 10;
#while(index<pdfreader.getNumPages()):

#pageobj = pdfreader.getPage(index)
#text = pageobj.extractText()
#print(type(text))

#    text = text.encode('utf-8')
#    if text != "":
#      newfile.write(text)
#    index= index+1
#file.close()






#for line in fileinput.FileInput("file",inplace=1):
#    if line.rstrip():
#        print(line)
#newfile = open("TheHelpConversion.txt","r")
#message = newfile.read()
#print(message)
#newfile.close()
