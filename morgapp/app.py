"""
Main app behavior
TODO : Setup layout
"""
import tkinter as tk

from command import MasterCommand
from workframe import WorkFrame
from statusbar import StatusBar
from spacebar import SpaceBar


class Application(tk.Tk):
    """ Class Application """

    def __init__(self):
        """ Main window constructor """
        tk.Tk.__init__(self)  # constructeur de la classe parente
        # self.root = tk.Tk()
        self.title("Morg")
        self.geometry("800x800")
        self.wm_iconbitmap("morgapp\\Notepad.ico")
        self.minsize(width=800, height=800)

        workframe_frame = WorkFrame(self)
        statusbar_frame = StatusBar(self)
        spacebar_frame = SpaceBar(self)

        workframe_frame.pack()
        statusbar_frame.pack()
        spacebar_frame.pack()

        # MODE Binding
        MasterCommand(self, workframe_frame, statusbar_frame, spacebar_frame)

        self.mainloop()


if __name__ == "__main__":

    Application()  # instanciation de l'objet application
