import PyPDF2

newfile = open("TheHelpConversion.txt","w")
file = open("TheHelp.pdf","rb")
pdfreader = PyPDF2.PdfFileReader(file)
#print(pdfreader.getNumPages())
index = 0;
while(index<pdfreader.getNumPages()):

    pageobj = pdfreader.getPage(index)
    #print(pageobj.extractText())
    newfile.write(pageobj.extractText())
    index= index+1;
file.close()
newfile.close()
