"""
Layout Module
"""
import tkinter as tk
from command import FileCommand


class Layout(tk.Frame):
    """
    Class Files
    """

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.parent = parent
        self.init_ui()

    def init_ui(self):
        """
        Fonction init_ui
        """

        self.parent.title("File dialog")
        self.pack(fill=tk.BOTH, expand=1)

        menubar = tk.Menu(self.parent)
        self.parent.config(menu=menubar)

        file_menu = tk.Menu(menubar)
        file_menu.add_command(label="Save", command=FileCommand.save_file)
        file_menu.add_command(label="Open", command=FileCommand.open_file)
        menubar.add_cascade(label="File", menu=file_menu)

        self.txt = tk.Text(self)
        self.txt.pack(fill=tk.BOTH, expand=1)


ROOT = tk.Tk()

TOP = tk.Frame(ROOT)
TOP.pack(fill=tk.BOTH, expand=1)

BOTTOM = tk.Frame(ROOT)
BOTTOM.pack()

# ex = Files(ROOT)
# ex.pack(side="bottom")

ROOT.geometry("300x250+300+300")
ROOT.mainloop()
