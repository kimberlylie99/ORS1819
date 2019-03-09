import PyPDF2
import fileinput

newfile = open("CareerFairConversion.txt","wb")
file = open("Career Fair Crash Course.pdf","rb")
pdfreader = PyPDF2.PdfFileReader(file)
#print(pdfreader.getNumPages())
index = 0;
while(index<pdfreader.getNumPages()):

    pageobj = pdfreader.getPage(index)
    #pageobj.extractText()
    text = pageobj.extractText()
    text = text.encode('utf-8')
    newfile.write(text)
    index= index+1
file.close()

#for line in fileinput.FileInput("file",inplace=1):
#    if line.rstrip():
#        print(line)
newfile = open("CareerFairConversion.txt","r")
message = newfile.read()
print(message)
newfile.close()
