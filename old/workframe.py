"""
This module implements the spacebar widget.
TODO : make Work frame 
"""

import tkinter as tk


class WorkFrame(tk.Frame):
    """
    This class implements a Workframe.
    """

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.text_area = tk.Text(self)
        self.scroll_bar = tk.Scrollbar(self.text_area)

        # Scrollbar will adjust automatically according to the content
        self.scroll_bar.config(command=self.text_area.yview)
        self.text_area.config(yscrollcommand=self.scroll_bar.set)
        self.text_area.grid_rowconfigure(0, weight=1)
        self.text_area.grid_columnconfigure(0, weight=1)
        self.text_area.pack()
        self.scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)


if __name__ == "__main__":

    ROOT = tk.Tk()
    FRAME = WorkFrame(ROOT)
    FRAME.pack(side=tk.TOP)
    ROOT.mainloop()
