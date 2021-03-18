import PyPDF2 


pdfFile = open('bpl.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
#print(dir(pdfReader))
page = pdfReader.numPages
text = pdfReader.getPage(0).extractText()
print(text)