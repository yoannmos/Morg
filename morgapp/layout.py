"""
Layout Module
"""
import tkinter
from command import FileCommand


class Layout(tkinter.Frame, FileCommand):
    """
    Class Files
    """

    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent)
        FileCommand.__init__(self)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        """
        Fonction init_ui
        """

        self.parent.title("File dialog")
        self.pack(fill=tkinter.BOTH, expand=1)

        menubar = tkinter.Menu(self.parent)
        self.parent.config(menu=menubar)

        file_menu = tkinter.Menu(menubar)
        file_menu.add_command(label="Save", command=self.save_command)
        file_menu.add_command(label="Open", command=self.open_command)
        menubar.add_cascade(label="File", menu=file_menu)

        self.txt = tkinter.Text(self)
        self.txt.pack(fill=tkinter.BOTH, expand=1)


ROOT = tkinter.Tk()

TOP = tkinter.Frame(ROOT)
TOP.pack(fill=tkinter.BOTH, expand=1)

BOTTOM = tkinter.Frame(ROOT)
BOTTOM.pack()

# ex = Files(ROOT)
# ex.pack(side="bottom")

ROOT.geometry("300x250+300+300")
ROOT.mainloop()
