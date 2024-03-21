from gettext import install

import pip
import pypdf
import pyttsx3
import PyPDF2
import camelot
import pypdf
#pip install pypdf<3.0.0
#pip install camelot-py[base]
file=open ("eries_13.pdf",mode="rb")
pdf_reader=pypdf.PdfReader(file)
pages=pdf_reader._get_page(1)
print(pages)
melo=pyttsx3.init()
#for i in range (1,pages):
page=pdf_reader._get_page(1)
text=page.extract_text()
melo.say(text)
#melo.say("Welcome to pycharm, the project has started running you can make your audiobook using pyhton?")
melo.runAndWait()