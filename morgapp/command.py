"""
command Module
"""
import tkinter

class MasterCommand:
    """
    Class Master Command
    """

    def __init__(self):

    def insert_commande(self)
    
    



class FileCommand:
    """
    Class File Command
    """

    def __init__(self):
        self.txt = tkinter.Text(self)
        self.txt.pack(fill=tkinter.BOTH, expand=1)

    def read_command(self, filename):
        """
        Fonction read_file
        """

        f_opened = open(filename, "r")
        text = f_opened.read()
        return text

    def open_command(self):
        """
        Fonction open command
        """

        ftypes = [("Python files", "*.py"), ("All files", "*")]
        dlg = tkinter.filedialog.Open(self, filetypes=ftypes)
        fl_show = dlg.show()

        if fl_show != "":
            text = self.read_command(fl_show)
            self.txt.insert(tkinter.END, text)

    def save_command(self):
        """
        Fonction save_command
        """
        file = tkinter.filedialog.asksaveasfile(mode="w")
        if file:
            data = self.txt.get("1.0", tkinter.END + "-1c")
            file.write(data)
            file.close()
