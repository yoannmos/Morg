"""
Command Module
"""

import tkinter as tk
from settings import SETTINGS


class MasterCommand(tk.Frame):
    """
    Class Master Command
    """

    def __init__(self, root, window, statusbar, spacebar):
        tk.Frame.__init__(self, root)

        self.root = root
        self.window = window
        self.status_bar = statusbar
        self.spacebar = spacebar

        # self.selected_mode = "NORMAL"
        self.set_mode("NORMAL")

        self.space_key_binding = SETTINGS["Commande"]["space_key_binding"]
        self.escape_key_binding = SETTINGS["Commande"]["escape_key_binding"]
        self.insert_key_binding = SETTINGS["Commande"]["insert_key_binding"]

        self.update_mode_label()
        # MODE Binding
        self.root.bind(self.space_key_binding, self.space_key)
        self.root.bind(self.escape_key_binding, self.escape_key)
        for k in self.insert_key_binding:
            self.root.bind(k, self.insert_key)

        self.pack()

    def update_mode_label(self):
        """
        Update mode label
        """
        # TODO : Adapt to real status bar, MODE label
        self.status_bar["text"] = self.selected_mode

    def set_mode(self, mode):
        """
        set_mode
        """
        # TODO : Disapear/ Reapear space bar
        if mode == "SPACE":
            self.selected_mode = "SPACE"
            self.spacebar.pack()
            self.window["state"] = "disabled"
            self.spacebar["state"] = "normal"

        elif mode == "NORMAL":
            self.selected_mode = "NORMAL"
            self.spacebar.pack_forget()
            self.window["state"] = "normal"
            self.spacebar["state"] = "disabled"

        elif mode == "INSERT":
            self.selected_mode = "INSERT"
            self.spacebar.pack_forget()
            self.window["state"] = "normal"
            self.spacebar["state"] = "disabled"

        # Update status bar
        self.update_mode_label()

    def space_key(self, event):
        """
        space_key
        """
        if self.selected_mode == "NORMAL":
            self.set_mode("SPACE")
        else:
            return

        print("pressed", repr(event.char))

    def escape_key(self, event):
        """
        escape_key
        """
        self.set_mode("NORMAL")
        print("pressed", repr(event.char))

    def insert_key(self, event):
        """
        insert_key
        """
        if self.selected_mode == "NORMAL":
            self.set_mode("INSERT")
        else:
            return
        print("pressed", repr(event.char))


if __name__ == "__main__":

    ROOT = tk.Tk()

    FRAME_1 = tk.Label(ROOT, text="<Window>")
    FRAME_2 = tk.Label(ROOT)
    FRAME_3 = tk.Label(ROOT, text="<Spacebar>)")

    FRAME_1.pack()
    FRAME_2.pack()
    FRAME_3.pack()

    COM = MasterCommand(ROOT, FRAME_1, FRAME_2, FRAME_3)

    ROOT.mainloop()
