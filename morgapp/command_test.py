"""
Module doc
"""
import tkinter


class Application(tkinter.Frame):
    """
    App
    """

    space_key_binding = "<space>"
    escape_key_binding = "<Escape>"
    insert_key_binding = [
        "a",  # Append text following current cursor position
        "A",  # Append text to the end of current line
        "i",  # Insert text before the current cursor position
        "I",  # Insert text at the beginning of the cursor line
        "o",  # Open up a new line following the current line and add text there
        "O",  # Open up a new line in front of the current line and add text there
    ]

    def __init__(self, master):
        tkinter.Frame.__init__(self, master)

        self.master.minsize(width=800, height=800)
        self.master.config()
        self.window = tkinter.Text(ROOT, state="normal", width=80, height=24)
        self.powerbar = tkinter.Text(ROOT, state="normal", width=80, height=4)

        # -----------------------------------------------------------------------------
        # MODE Binding

        self.master.bind(self.space_key_binding, self.space_key)
        self.master.bind(self.escape_key_binding, self.escape_key)
        for k in self.insert_key_binding:
            self.master.bind(k, self.insert_key)
        # -----------------------------------------------------------------------------
        self.main_frame = tkinter.Frame()

        self.selected_mode = "NORMAL"
        self.set_mode("NORMAL")
        self.pack()

    def set_mode(self, mode):
        """
        set_mode
        """
        if mode == "SPACE":
            self.selected_mode = "SPACE"
            self.window["state"] = "disabled"
            self.powerbar["state"] = "normal"

        elif mode == "NORMAL":
            self.selected_mode = "NORMAL"
            self.window["state"] = "disabled"
            self.powerbar["state"] = "disabled"

        elif mode == "INSERT":
            self.selected_mode = "INSERT"
            self.window["state"] = "normal"
            self.powerbar["state"] = "disabled"

    def space_key(self, event):
        """
        space_key
        """
        if self.selected_mode == "NORMAL":
            self.set_mode("SPACE")
        else:
            return

        print("pressed", repr(event.char))
        print(self.selected_mode, " activated")

    def escape_key(self, event):
        """
        escape_key
        """
        self.set_mode("NORMAL")

        print("pressed", repr(event.char))
        print(self.selected_mode, " activated")

    def insert_key(self, event):
        """
        insert_key
        """
        if self.selected_mode == "NORMAL":
            self.set_mode("INSERT")

        print("pressed", repr(event.char))
        print(self.selected_mode, " activated")


if __name__ == "__main__":
    ROOT = tkinter.Tk()
    APP = Application(ROOT)
    APP.mainloop()

# ---------------------------------------------------------------------
# root = tkinter.Tk()
# window = tkinter.Text(root, state="normal", width=80, height=24)
# bar = tkinter.Text(root, state="normal", width=80, height=4)

# frame = tkinter.Frame(root, width=100, height=100)
