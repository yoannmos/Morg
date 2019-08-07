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

        spacebar_frame = SpaceBar(self)
        spacebar_frame.pack(side=tk.BOTTOM)
        statusbar_frame = StatusBar(self)
        statusbar_frame.pack(side=tk.BOTTOM)
        workframe_frame = WorkFrame(self)
        workframe_frame.pack(side=tk.BOTTOM)

        # MODE Binding
        master_com = MasterCommand(
            self, workframe_frame, statusbar_frame, spacebar_frame
        )
        statusbar_frame.set_mode(master_com.selected_mode)

        self.mainloop()

    #     self.selected_mode = "NORMAL"
    #     self.set_mode("NORMAL")
    #     self.pack()

    # def set_mode(self, mode):
    #     """
    #     set_mode
    #     """
    #     if mode == "SPACE":
    #         self.selected_mode = "SPACE"
    #         self.window["state"] = "disabled"
    #         self.powerbar["state"] = "normal"

    #     elif mode == "NORMAL":
    #         self.selected_mode = "NORMAL"
    #         self.window["state"] = "disabled"
    #         self.powerbar["state"] = "disabled"

    #     elif mode == "INSERT":
    #         self.selected_mode = "INSERT"
    #         self.window["state"] = "normal"
    #         self.powerbar["state"] = "disabled"

    # def space_key(self, event):
    #     """
    #     space_key
    #     """
    #     if self.selected_mode == "NORMAL":
    #         self.set_mode("SPACE")
    #     else:
    #         return

    #     print("pressed", repr(event.char))
    #     print(self.selected_mode, " activated")

    # def escape_key(self, event):
    #     """
    #     escape_key
    #     """
    #     self.set_mode("NORMAL")

    #     print("pressed", repr(event.char))
    #     print(self.selected_mode, " activated")

    # def insert_key(self, event):


# Programme principal :
if __name__ == "__main__":

    Application()  # instanciation de l'objet application
