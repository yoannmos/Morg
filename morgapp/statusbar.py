"""
This module implements the statusbar widget.
"""

import tkinter as tk


class StatusBar(tk.Frame):
    """
    This class implements a statusbar.
    """

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.config(border=1)

        self.msg = tk.Label(self, bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.msg.pack(side="left", expand=True, fill=tk.X)

        self.column = tk.Label(self, bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.column.config(text="Col: 0")
        self.column.pack(side="right", fill=tk.X)

        self.line = tk.Label(self, bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.line.config(text="Line: 1")
        self.line.pack(side="right", fill=tk.X)

        self.mode = tk.Label(self, bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.mode.config(text="NORMAL")
        self.mode.pack(side="right", fill=tk.X)

    def set_msg(self, data):
        """
        Set statusbar msg.
        """

        self.msg.config(text=data)
        self.msg.update_idletasks()

    def clear_msg(self):
        """
        Clear statusbar msg.
        """

        self.msg.config(text="")
        self.msg.update_idletasks()

    def set_column(self, col):
        """
        Set the column field with col.
        """

        self.column.config(text="Col: %s" % col)
        self.column.update_idletasks()

    def set_line(self, line):
        """
        Set the line field.
        """

        self.line.config(text="Line: %s" % line)
        self.line.update_idletasks()

    def set_mode(self, mode):
        """
        Set the mode field.
        """

        self.mode.config(text=mode)
        self.mode.update_idletasks()


if __name__ == "__main__":

    ROOT = tk.Tk()
    FRAME = StatusBar(ROOT)
    FRAME.pack(side=tk.TOP)
    ROOT.mainloop()
