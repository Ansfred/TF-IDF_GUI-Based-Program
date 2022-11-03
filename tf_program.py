import re
from tkinter import *
from tkinter import messagebox, ttk
from tkinter import scrolledtext as tkst
from datetime import date
from time import strftime

root = Tk()
root.geometry("1366x768")
root.title("Welcome User!")

'''
StringVar() : A class that is used to store a string value.
'''
input_file_content_textBox = StringVar()
word_to_be_searched_textBox = StringVar()



class TF_Page:
    def __init__(self, top=None):
        '''
        The Toplevel widget is used to create and display the toplevel windows which are directly managed by the window manager.
        '''
        top.geometry("1366x768")
        top.resizable(0, 0)         # To create a fixed size window
        top.title("TF Window")

        self.label1 = Label(root)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./images/TF_background.png")
        self.label1.configure(image=self.img)
        
        self.clock = Label(root)
        self.clock.place(relx=0.875, rely=0.03, width=150, height=30)
        self.clock.configure(font="-family {Cambria Math} -size 16")
        self.clock.configure(foreground="#000000")
        self.clock.configure(background="#ffffff")

        '''
        Creating a text entry box and placing it on the screen.
        '''
        self.entry1 = Entry(root)       # A widget that is used to enter text strings
        # ISSUE: Set max-width: 850 and max-height: 167.5. Use ScrollBar
        self.entry1.place(relx=0.183, rely=0.165, width=860, height=167.5)
        self.entry1.configure(font="-family {Cambria Math} -size 20")
        self.entry1.configure(relief="flat")
        self.entry1.configure(background="#d9d9d9")
        self.entry1.configure(textvariable=input_file_content_textBox)
        
        '''
        Creating a text entry box and placing it on the screen.
        '''
        self.entry2 = Entry(root)
        self.entry2.place(relx=0.53, rely=0.4725, width=250, height=50)
        self.entry2.configure(font="-family {Cambria Math} -size 20")
        self.entry2.configure(relief="flat")
        self.entry2.configure(background="#d9d9d9")
        self.entry2.configure(textvariable=word_to_be_searched_textBox)

        '''
        Creating a button and placing it on the screen.
        '''
        self.button1 = Button(root)
        self.button1.place(relx=0.43, rely=0.78, width=190, height=55)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#ffffff")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#000000")
        self.button1.configure(background="#ffffff")
        self.button1.configure(font="-family {Bookman Old Style} -weight {bold} -size 18")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""SEARCH""")
        self.button1.configure(command=self.searchWord)


    def time(self):
        """
        It takes the current time and displays it in the clock label
        """
        string = strftime("%H:%M:%S %p")
        self.clock.config(text=string)
        self.clock.after(1000, self.time)


    def searchWord(self, Event=None):
        """
        It takes the input from the user, finds all the words in the input, stores them in a dictionary, and then finds the frequency of the word to be searched.
        """
        input_file_content = input_file_content_textBox.get()
        word_to_be_searched = word_to_be_searched_textBox.get()
        
        if input_file_content != "" and word_to_be_searched != "":
            # Initializing an empty dictionary and storing frequency of all words in it.
            frequency_of_words = {}
            words = re.findall(r'\b[a-z]{1,20}\b', input_file_content)

            # Calculating frequency of all the words in our corpus.
            for word in words:
                word_count = frequency_of_words.get(word, 0)
                frequency_of_words[word] = word_count + 1

            list_of_words = frequency_of_words.keys()
            list_of_frequencies = frequency_of_words.values()
            total_words_count = 0
            for word in list_of_frequencies:
                total_words_count += word

            if list_of_words.__contains__(word_to_be_searched):
                display_count = frequency_of_words.get(word_to_be_searched)
                display_percentage = (display_count / total_words_count) * 100
                
                '''
                Creating a text entry box and placing it on the screen.
                '''
                entry3 = Entry(root)
                entry3.place(relx=0.26775, rely=0.6375, width=240, height=40)
                entry3.configure(foreground="#000000")
                entry3.configure(background="#d9d9d9")
                entry3.configure(font="-family {Cambria Math} -size 20")
                entry3.configure(relief="flat")
                entry3.insert(0, display_count)

                '''
                Creating a text entry box and placing it on the screen.
                '''
                entry4 = Entry(root)
                entry4.place(relx=0.64725, rely=0.6375, width=240, height=40)
                entry4.configure(foreground="#000000")
                entry4.configure(background="#d9d9d9")
                entry4.configure(font="-family {Cambria Math} -size 20")
                entry4.configure(relief="flat")
                entry4.insert(0, display_percentage)

            else:
                messagebox.showerror("Error!!", "Desired word cannot be found!")
                page1.entry2.delete(0, END)


def exit():
    """
    If the user clicks the "Yes" button, the program will close. If the user clicks the "No" button, the program will not close.
    """
    exit_confirmation = messagebox.askyesno("Exit", "Are you sure?", parent=root)
    if exit_confirmation == True:
        root.destroy()

# A protocol that is used to handle the interaction between the application and the window manager.
root.protocol("WM_DELETE_WINDOW", exit)


page1 = TF_Page(root)
page1.time()
root.bind("<Return>", TF_Page.searchWord)
root.mainloop()
