"""
command Module
"""
import tkinter
import keyboard  # using module keyboard


class MasterCommand:
    """
    Class Master Command
    """

    def __init__(self):
        while True:  # making a loop
            try:  # used try so that if user pressed other than the given key error will not be shown
                if keyboard.is_pressed("q"):  # if key 'q' is pressed
                    print("You Pressed A Key!")
                    break  # finishing the loop
                else:
                    pass
            except:
                break  # if user pressed a key other than the given key the loop will break

    def insert_commande(self):
        return


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

        ftypes = [("Python files", "*.py"), ("Org files", "*.org"), ("All files", "*")]
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
