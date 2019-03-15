import PyPDF2
import fileinput

newfile = open("TheHelpConversion.txt","wb")
file = open("TheHelp.pdf","rb")
pdfreader = PyPDF2.PdfFileReader(file)
#print(pdfreader.getNumPages())
index = 0;
while(index<pdfreader.getNumPages()):

    pageobj = pdfreader.getPage(index)
    #pageobj.extractText()
    text = pageobj.extractText()
    text = text.encode('utf-8')
    if text != "":
      newfile.write(text)
    index= index+1
file.close()

#for line in fileinput.FileInput("file",inplace=1):
#    if line.rstrip():
#        print(line)
#newfile = open("TheHelpConversion.txt","r")
#message = newfile.read()
#print(message)
#newfile.close()
