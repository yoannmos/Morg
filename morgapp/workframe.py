"""
This module implements the spacebar widget.
TODO : make Work frame Commande group implementation
"""

import tkinter as tk


class WorkFrame(tk.Frame):
    """
    This class implements a Workframe.
    """

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.text_area = tk.Text(self)
        self.text_area.pack()


if __name__ == "__main__":

    ROOT = tk.Tk()
    FRAME = WorkFrame(ROOT)
    FRAME.pack(side=tk.TOP)
    ROOT.mainloop()
