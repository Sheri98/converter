from tkinter import *
from tkinter import filedialog
import tkinter.font as font
from pdf2docx import parse
from threading import *
from docx2pdf import convert

def center(e):
    w = int(root.winfo_width() / 3.5) # get root width and scale it ( in pixels )
    s = 'Pdf2Docx2Pdf'.rjust(w//2)
    root.title(s)


def startDocxThread():
    thread = Thread(target=DocxConverted)
    thread.start()
def startPDFThread():
    thread = Thread(target=PdfConverted())
    thread.start()
root = Tk()
root.minsize(width=400, height=300)
root.maxsize(width=400, height=300)
root.bind("<Configure>", center)
myFont = font.Font(family='Helvetica')

def DocxConverted():
    convert(root.filename,"file.pdf")
    root.filename = ""

def PdfConverted():
    parse(root.filename, "C:\\Users\\Shravan Sheri\\Documents\\file.docx")
    root.filename = ""
def DocxConverter():

    root.filename = filedialog.askopenfilename(initialdir="D:/pycharmprojects/GUI/images", title="Select A File",filetypes=(("DOCX", "*.docx"), ("All files", "*.*")))
    Docxlabel = Label(text="DOCX Filenname:" + "\n" + root.filename)
    Docxlabel.grid(row=3, column=0, padx=10, pady=10)
    Convertbtn = Button(text="Convert",command=startDocxThread)
    Convertbtn.grid(row=4,column=0,padx=10,pady=3)

def PdfConverter():
    root.filename = filedialog.askopenfilename(initialdir="D:/pycharmprojects/GUI/images", title="Select A File",
                                               filetypes=(("DOCX", "*.pdf"), ("All files", "*.*")))
    Docxlabel = Label(text="PDF Filenname:" + "\n" + root.filename)
    Docxlabel.grid(row=3, column=0, padx=10, pady=10)
    Convertbtn = Button(text="Convert", command=startPDFThread)
    Convertbtn.grid(row=4, column=0, padx=10, pady=3)


Converttopdf = Button(root,font=myFont,text="DOCXtoPDF",command =DocxConverter)
Converttopdf.grid(row=1,column=0,pady = 5,padx = 110,columnspan=1)

Converttodocx = Button(root,font=myFont,text="PDFtoDOCX",command =PdfConverter)
Converttodocx.grid(row=2, column=0,pady = 5,padx = 110,columnspan=1)

root.mainloop()