from cStringIO import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import os
import re

root = "" # Enter the root directory 
pdf_folder = root + "PDFs/"  #PDF filed directory
text_folder = root + "Text/" #Converted Text Directory

#converts pdf, returns its text content as a string
def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = file(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return re.sub('\W+',' ', text )

def get_pdfs():
    pdf_files = []
    for path, subdirs, files in os.walk(pdf_folder):
        for name in files:
            _, file_extension = os.path.splitext(name)
            if file_extension == ".pdf":
                pdf_files.append(os.path.join(path, name))
    return pdf_files

def convertMultiple():
    pdfs = get_pdfs()
    for pdf in pdfs:
        text = convert(pdf) #get string of text content of pdf
        file_name , _ = os.path.splitext(os.path.basename(pdf))
        textFilename = file_name + ".txt"
        textFile = open(text_folder + textFilename, "w") #make text file
        textFile.write(text) #write text to text file

if __name__ == '__main__':
    convertMultiple()