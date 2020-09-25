
# How to Create a Simple Chat Bot GUI Using Python
#In this article I will show you how to build a graphical user interface (GUI) using the Python programming language 
#that you can use for a chat bot. So no, this won’t be an actual chat bot, I will be focusing on just the graphical user 
#interface components. This is a good exercise to get familiar with creating GUI’s using Python. The graphical user interface (GUI)
# is a form of user interface that allows users to interact with electronic devices through graphical icons and audio indicators such as primary notation, instead of text-based user interfaces, typed command labels 
#or text navigation. -wikipedia

# Description: This is a chat bot GUI
#Next I will load the library that I will need to create this GUI.
from tkinter import *
# Next I will create the tkinter object. This represents the parent window.
root = Tk()

# Now, I will give the Window a title, a shape, and make it such that it can’t be resized.
root.title("Chat Bot")
root.geometry("400x500")
root.resizable(width=FALSE, height=FALSE)

#Let’s create the main menu.
main_menu = Menu(root)
# Create the submenu 
file_menu = Menu(root)

# Add commands to submenu
file_menu.add_command(label="New..")
file_menu.add_command(label="Save As..")
file_menu.add_command(label="Exit")
main_menu.add_cascade(label="File", menu=file_menu)
#Add the rest of the menu options to the main menu
main_menu.add_command(label="Edit")
main_menu.add_command(label="Quit")
root.config(menu=main_menu)

# Create a window for the conversation and place it on the parent window.
chatWindow = Text(root, bd=1, bg="black",  width="50", height="8", font=("Arial", 23), foreground="#00ffff")
chatWindow.place(x=6,y=6, height=385, width=370)
#Create the text area where the messages will be entered and place it on the parent window.
messageWindow = Text(root, bd=0, bg="black",width="30", height="4", font=("Arial", 23), foreground="#00ffff")
messageWindow.place(x=128, y=400, height=88, width=260)

#Create a scroll bar and place it on the parent window.
scrollbar = Scrollbar(root, command=chatWindow.yview, cursor="star")
scrollbar.place(x=375,y=5, height=385)
#Create a button to send the message and place it on the parent window.
Button= Button(root, text="Send",  width="12", height=5,
                    bd=0, bg="#0080ff", activebackground="#00bfff",foreground='#ffffff',font=("Arial", 12))
Button.place(x=6, y=400, height=88)
#Run the main loop.
root.mainloop()

#============================ References======================================== #
#[1]How to Create a Simple Chat Bot GUI Using Python
# https://morioh.com/p/b24bf58a2e2e?f=5c21fb01c16e2556b555ab32&fbclid=IwAR2PWopwoJv_pZA-_8yfZJNrCYgFidY9jjLgfbRJ1CkFpBaGW360z2uLdZk
#[3] Chatbot using Python | ML based Chatbot | Part 1 ( HINDI )
# https://www.youtube.com/watch?v=VUubtrSSiPg
#[4] Chatbot using Python | ML based Chatbot | Part 2 ( HINDI )
#https://www.youtube.com/watch?v=NDX6gLajRsI