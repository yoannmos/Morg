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

        self.mode = tk.Label(self, bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.mode.config(text="Col: 0")
        self.mode.pack(side="left", expand=True, fill=tk.X)

        self.column = tk.Label(self, bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.column.config(text="Col: 0")
        self.column.pack(side="right", fill=tk.X)

    def set_mode(self, data):
        """
        Set statusbar msg.
        """

        self.mode.config(text=data)
        self.mode.update_idletasks()

    def set_column(self, col):
        """
        Set the column field with col.
        """

        self.column.config(text="Col: %s" % col)
        self.column.update_idletasks()


if __name__ == "__main__":

    ROOT = tk.Tk()
    FRAME = SpaceBar(ROOT)
    FRAME.pack(side=tk.TOP)
    ROOT.mainloop()
