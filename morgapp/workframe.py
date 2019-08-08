"""
This module implements the spacebar widget.
TODO : make Work frame Commande group implementation
"""

import tkinter as tk
import tkinter.scrolledtext as tkst
from settings import SETTINGS


class WorkFrame(tk.Frame):
    """
    This class implements a Workframe.
    """

    tagInit = False
    commandsToRemove = SETTINGS["Commande"]["normal_key_forbiden"]

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.label_title = tk.Label(master=self, text="workframe")

        self.access = "R"
        self.active_buffer = tkst.ScrolledText(master=self)

        self.label_title.pack()
        self.active_buffer.pack()

    def read_only(self):
        """
        Read only methode
        """
        # TODO: Specification on wich key
        if self.access == "R":
            for comtormve in self.commandsToRemove:
                self.active_buffer.bind(comtormve, lambda e: "break")
            self.active_buffer.unbind("<Escape>")
            self.active_buffer.unbind("<Space>")
            self.access = "W"
            self.active_buffer.pack()
        else:
            self.active_buffer.unbind("<Key>")
            self.access = "R"


if __name__ == "__main__":

    ROOT = tk.Tk()
    FRAME = WorkFrame(ROOT)
    BUTTON = tk.Button(master=FRAME, text="SWITCH", command=FRAME.read_only)
    BUTTON.pack()
    FRAME.pack(side=tk.TOP)
    ROOT.mainloop()
