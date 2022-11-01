__author__ = "Ansfred"
import os
from tkinter import *
from tkinter import messagebox

main = Tk()
main.geometry("1366x768")
main.title("TF - IDF Assignment")
main.resizable(0, 0)

def exit():
    """
    If the user clicks the "Yes" button, the program will close. If the user clicks the "No" button, the program will not close.
    """
    exit_confirmation = messagebox.askyesno("Exit", "Are you sure?", parent=main)
    if exit_confirmation == True:
        main.destroy()

# A protocol that is used to handle the interaction between the application and the window manager.
main.protocol("WM_DELETE_WINDOW", exit)

def tf_window():
    """
    It opens a new window, runs a python script, then closes the new window and reopens the original window
    """
    main.withdraw()         # Hides the root window
    os.system("python tf_program.py")
    main.deiconify()        # Make the root window reappear

def idf_window():
    """
    It opens a new window, runs a python script, then closes the new window and reopens the original window
    """
    main.withdraw()         # Hides the root window
    os.system("python idf_program.py")
    main.deiconify()        # Make the root window reappear

# Home image
label1 = Label(main)        # It creates a label widget
label1.place(relx=0, rely=0, width=1366, height=768)
img = PhotoImage(file="./images/home_background.png")
label1.configure(image=img)

# TF window mini-image -> Redirects
button1 = Button(main)      # It creates a button widget
button1.place(relx=0.221, rely=0.36, width=300, height=300)
button1.configure(relief="flat")
button1.configure(overrelief="flat")
button1.configure(activebackground="#ffffff")
button1.configure(cursor="hand2")
button1.configure(foreground="#ffffff")
button1.configure(background="#ffffff")
button1.configure(borderwidth="0")
img2 = PhotoImage(file="./images/home_background_sub1.png")
button1.configure(image=img2)
button1.configure(command=tf_window)

# IDF window mini-image -> Redirects
button2 = Button(main)      # It creates a button widget
button2.place(relx=0.571, rely=0.36, width=300, height=300)
button2.configure(relief="flat")
button2.configure(overrelief="flat")
button2.configure(activebackground="#ffffff")
button2.configure(cursor="hand2")
button2.configure(foreground="#ffffff")
button2.configure(background="#ffffff")
button2.configure(borderwidth="0")
img3 = PhotoImage(file="./images/home_background_sub2.png")
button2.configure(image=img3)
button2.configure(command=idf_window)

# A method that is used to run the main window.
main.mainloop()