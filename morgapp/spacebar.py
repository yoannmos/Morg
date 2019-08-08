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

        self.key = tk.Label(self, bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.key.config(text="Col: 0")
        self.key.pack(side="right", fill=tk.X)

    def set_mode(self, data):
        """
        Set statusbar msg.
        """

        self.mode.config(text=data)
        self.mode.update_idletasks()

    def set_key(self, keyboard_entry):
        """
        Set the key field with col.
        """

        self.key.config(text=keyboard_entry)
        self.key.update_idletasks()


if __name__ == "__main__":

    ROOT = tk.Tk()
    FRAME = SpaceBar(ROOT)
    FRAME.pack(side=tk.TOP)
    ROOT.mainloop()
