"""
This module implements the spacebar widget.
TODO : make Space bar Commande group implementation
"""

import tkinter as tk


class SpaceBar(tk.Frame):
    """
    This class implements a spacebar.
    """

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.config(border=1)

        self.menu = tk.Label(self, bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.menu.config(text="Col: 0")
        self.menu.pack(side="top", fill=tk.X)

        self.key = tk.Label(self, bd=1, anchor=tk.W)
        self.key.config(text="<ENTER KEY>")
        self.key.pack(anchor=tk.W, side="left", fill=tk.Y)

    def set_menu(self, data):
        """
        Set statusbar msg.
        """

        self.menu.config(text=data)
        self.menu.update_idletasks()

    def set_key(self, data):
        """
        Set the key field with col.
        """

        self.key.config(text=data)
        self.key.update_idletasks()


if __name__ == "__main__":

    ROOT = tk.Tk()
    FRAME = SpaceBar(ROOT)
    FRAME.pack(side=tk.TOP)
    ROOT.mainloop()
