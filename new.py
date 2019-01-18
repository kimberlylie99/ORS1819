import PyPDF2

newfile = open("TheHelpConversion.txt","w")
file = open("TheHelp.pdf","rb")
pdfreader = PyPDF2.PdfFileReader(file)
print(pdfreader.getNumPages())
pageobj = pdfreader.getPage(1)
print(pageobj.extractText())
newfile.write(pageobj.extractText())
file.close()
newfile.close()
