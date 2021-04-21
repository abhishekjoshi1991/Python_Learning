# Working with PDF Files

'''
All pdf can not be read by python. To read pdf file we are using PyPDF2 package.
There are other paid packages that may read all possible pdf file but PyPDF2 has some limitations
'''

import PyPDF2

#************************************************************************************************************
# To read PDF file
#************************************************************************************************************

f = open('example.pdf','rb')  #open pdf file in binary reading mode
pdf_read = PyPDF2.PdfFileReader(f) #created PdfFileReader object

print(pdf_read.numPages)

#to grab first page pass the page number being first page is zero index
page_one = pdf_read.getPage(0) #created object of getPage

#to display text in this first page
page_one_text = page_one.extractText()
print(page_one_text)

#************************************************************************************************************
# To read PDF file
#************************************************************************************************************
