import pyttsx3
import PyPDF2
from tkinter.filedialog import *
from time import sleep


print("Please select pdf that is purely pdf not cam scanned one!")
sleep(3)

book = askopenfile()
if not book:
    print("please select the pdf!")

pdfreader = PyPDF2.PdfFileReader(book)
pages = pdfreader.numPages


for num in range(0, pages):
    page = pdfreader.getPage(num)
    text = page.extractText()
    player = pyttsx3.init()
    player.say(text)
    player.runAndWait()
