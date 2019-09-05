#! bin/env python3
#graphicinterface.py
"""

"""
import tkinter as tk

# Set GUI defaults
fontspec = r'font=("Fira Code", 18)'

# Construct Main GUI Interface Window
window = tk.Tk()
window.title("Prioritree")
window.configure(background='black')
label = tk.Label(window, text = "Welcome to Prioritree!", font=("Fira Code", 18), fg='white', bg='black').pack()

# def displaysplash():
#     """
#     Displays the splash screen upon startup
#     :return: None
#     """
#     splashscreen = tk.Tk()
#     splashscreen.title("Welcome to Prioritree!")
#     splashscreen.configure(background='black')
#     # Add some text as a placeholder for an image widget
#     splashlabel = tk.Label(splashscreen, text = "placeholder text", font = "Fira Code", 18))
#


## Run the script to show the window until the user interacts
window.mainloop()

# from tkinter import *
#
# # Instantiate an object of class Tk() called `window`
# root = Tk()
# root.title("Prioritree")
# root.geometry('600x150') ## Width x Height (pixels?)
#
# # Include a label of text within the window and place it on a grid
# lbl = Label(root, text = "Hello ==> Welcome to Priortree!", font=("Fira Code", 18))
# lbl.grid(column=0, row=0)
#
# # Make some buttons and event handlers:
# def clicked_button():
#     """
#     Event handler function for the button.
#     :param: None
#     :return: None
#     """
#     lbl.configure(text="The button was clicked!!!")
#
#
# btn = Button(root, text="Click Me!", font=("Fira Code", 18), fg="white", bg="black", command=clicked_button())
# btn.grid(column=1, row=0)
#
# # Run the interface window in mainloop() that waits for user interaction
# root.mainloop()

