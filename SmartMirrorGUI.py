############# LEGAL #############
#
#This program was created by Samuel Lomas, 2020
#I intend for this program to use the GPL (GNU public license) when it is published to github.
#I also have zero experience with TKinter, so expect this to be shoddy
#
############# IMPORTS ############
import tkinter as tk
import time
############# MAIN ##############
root = tk.Tk() #root widget, creates the window
screen_width = root.winfo_screenwidth() #next two lines are used to automatically scale the window
screen_height = root.winfo_screenheight()
root.geometry(str(screen_width) + "x" + str(screen_height)) #ditto.
root.state("zoomed")

w = tk.Label(root, text="Hello World!").pack()



############# START ###########
root.mainloop() #starts the GUI by entering a mainloop
