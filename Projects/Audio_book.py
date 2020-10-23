#Title = Make Audio book from any PDF using Python.
#Reference:https://morioh.com/p/42a6957afa8a?f=5c21fb01c16e2556b555ab32&fbclid=IwAR0QWBN--b-IlKDTZ0EAAkOyGWIT_8hLUqqZH-TOckslanJs1WSxkRIG1u8
#Modules = Frist of all you can install Three Modules.
#!pip install pywin32
#!pip install pyPDF2
#We can import two packages 
#importe pytsx3 and pyPDF2 


import pyttsx3
#It is a text-to-speech conversion library in Python
import PyPDF2 
#The PdfFileReader Class
from tkinter.filedialog import *
#tkinter.filedialog import askopenfilename from tkinter.messagebox import showerror class MyFrame(Frame):

book = askopenfilename() 
#Now we have to read the name of our pdf file from the user.We take the file name.
pdfreader=PyPDF2.PdfFileReader(book) 
#We intialize with the pdf reader.Its on object.In parentheses we pass the (book)
Pages= pdfreader.numPages 
#We get the number of pages pdf file.I will take a variable call pages.
for num in range(0, Pages):
    #We need to read all the data from each of the pages in the pdf.create a for loop
    page=pdfreader.getPage(num) 
    #Inside the for loop i will get all the single pages. 
    text=page.extractText() 
    #Now i need to convert the text or extract from the pdf.So i will a create a variable text  
    player=pyttsx3.init() 
    #Now we need to define text to speech to object .So i will take a object player and intialize the pyttsx3 
    player.say(text) 
    #I write the player and then say text
    player.runAndWait()
    #Lets now run your programme and ask for pdf file.Now it will ask for  
    
     
