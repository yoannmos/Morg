"""
mod
"""
import os
import tkinter

import tkinter.messagebox
import tkinter.filedialog

# from tkinter import *
# from tkinter.messagebox import *
# from tkinter.filedialog import *


class Notepad:
    """
    Notepad
    """

    ROOT = tkinter.Tk()

    # default window width and height
    window_width = 300
    window_height = 300
    __thisTextArea = tkinter.Text(ROOT)
    __thisMenuBar = tkinter.Menu(ROOT)
    __thisFileMenu = tkinter.Menu(__thisMenuBar, tearoff=0)
    __thisEditMenu = tkinter.Menu(__thisMenuBar, tearoff=0)
    __thisHelpMenu = tkinter.Menu(__thisMenuBar, tearoff=0)

    # To add scrollbar
    __thisScrollBar = tkinter.Scrollbar(__thisTextArea)
    __file = None

    def __init__(self, **kwargs):

        # Set icon
        try:
            self.ROOT.wm_iconbitmap("Morg/morgapp/Notepad.ico")
        except ValueError:
            print("No logo found")

        # Set window size (the default is 300x300)

        try:
            self.window_width = kwargs["width"]
        except KeyError:
            pass

        try:
            self.window_height = kwargs["height"]
        except KeyError:
            pass

        # Set the window text
        self.ROOT.title("Untitled - Notepad")

        # Center the window
        screen_width = self.ROOT.winfo_screenwidth()
        print(screen_width)
        screen_height = self.ROOT.winfo_screenheight()
        print(screen_height)
        # For left-alling
        left = (screen_width / 2) - (self.window_width / 2)

        # For right-allign
        top = (screen_height / 2) - (self.window_height / 2)

        # For top and bottom
        self.ROOT.geometry(
            "%dx%d+%d+%d" % (self.window_width, self.window_height, left, top)
        )

        # To make the textarea auto resizable
        self.ROOT.grid_rowconfigure(0, weight=1)
        self.ROOT.grid_columnconfigure(0, weight=1)

        # Add controls (widget)
        self.__thisTextArea.grid(sticky=tkinter.N + tkinter.E + tkinter.S + tkinter.W)

        # To open new file
        self.__thisFileMenu.add_command(label="New", command=self.__newFile)

        # To open a already existing file
        self.__thisFileMenu.add_command(label="Open", command=self.__openFile)

        # To save current file
        self.__thisFileMenu.add_command(label="Save", command=self.__saveFile)

        # To create a line in the dialog
        self.__thisFileMenu.add_separator()
        self.__thisFileMenu.add_command(label="Exit", command=self.__quitApplication)
        self.__thisMenuBar.add_cascade(label="File", menu=self.__thisFileMenu)

        # To give a feature of cut
        self.__thisEditMenu.add_command(label="Cut", command=self.__cut)

        # to give a feature of copy
        self.__thisEditMenu.add_command(label="Copy", command=self.__copy)

        # To give a feature of paste
        self.__thisEditMenu.add_command(label="Paste", command=self.__paste)

        # To give a feature of editing
        self.__thisMenuBar.add_cascade(label="Edit", menu=self.__thisEditMenu)

        # To create a feature of description of the notepad
        self.__thisHelpMenu.add_command(label="About Notepad", command=self.__showAbout)
        self.__thisMenuBar.add_cascade(label="Help", menu=self.__thisHelpMenu)

        self.ROOT.config(menu=self.__thisMenuBar)

        self.__thisScrollBar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        # Scrollbar will adjust automatically according to the content
        self.__thisScrollBar.config(command=self.__thisTextArea.yview)
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)

    def __quitApplication(self):
        self.ROOT.destroy()
        # exit()

    def __showAbout(self):
        tkinter.messagebox.showinfo("Notepad", "Test")

    def __openFile(self):

        self.__file = tkinter.filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")],
        )

        if self.__file == "":

            # no file to open
            self.__file = None
        else:

            # Try to open the file
            # set the window title
            self.ROOT.title(os.path.basename(self.__file) + " - Notepad")
            self.__thisTextArea.delete(1.0, tkinter.END)

            file = open(self.__file, "r")

            self.__thisTextArea.insert(1.0, file.read())

            file.close()

    def __newFile(self):
        self.ROOT.title("Untitled - Notepad")
        self.__file = None
        self.__thisTextArea.delete(1.0, tkinter.END)

    def __saveFile(self):

        if self.__file is None:
            # Save as new file
            self.__file = tkinter.filedialog.asksaveasfilename(
                initialfile="Untitled.txt",
                defaultextension=".txt",
                filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")],
            )

            if self.__file == "":
                self.__file = None
            else:

                # Try to save the file
                file = open(self.__file, "w")
                file.write(self.__thisTextArea.get(1.0, tkinter.END))
                file.close()

                # Change the window title
                self.ROOT.title(os.path.basename(self.__file) + " - Notepad")

        else:
            file = open(self.__file, "w")
            file.write(self.__thisTextArea.get(1.0, tkinter.END))
            file.close()

    def __cut(self):
        self.__thisTextArea.event_generate("<<Cut>>")

    def __copy(self):
        self.__thisTextArea.event_generate("<<Copy>>")

    def __paste(self):
        self.__thisTextArea.event_generate("<<Paste>>")

    def run(self):
        """
        run app
        """

        # Run main application
        self.ROOT.mainloop()


# Run main application
NOTEPAD = Notepad(width=600, height=400)

NOTEPAD.run()
