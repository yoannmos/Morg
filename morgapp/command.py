"""
Command Module
"""

import tkinter as tk
from settings import SETTINGS


class MasterCommand(tk.Frame):
    """
    Class Master Command
    """

    def __init__(self, root, workframe, statusbar, spacebar):
        tk.Frame.__init__(self, root)

        self.root = root
        self.workframe = workframe
        self.status_bar = statusbar
        self.spacebar = spacebar

        self.selected_mode = "INSERT"
        self.status_bar.set_mode(self.selected_mode)

        self.space_key_binding = SETTINGS["Commande"]["space_key_binding"]
        self.escape_key_binding = SETTINGS["Commande"]["normal_key_binding"]
        self.insert_key_binding = SETTINGS["Commande"]["insert_key_binding"]

        self.binding_key(root)

        self.pack()

    def update_mode(self):
        """ Update mode label """
        # TODO : Adapt to real status bar, MODE label
        self.status_bar.mode["text"] = self.selected_mode

    def binding_key(self, frame, access="ALL"):
        """ MODE Binding """
        # TODO: Delete insert mode character

        if access == "R":
            binding_access = frame.bind("<Key>", "pass")
            frame.bind("<Left>", (lambda e: None))
            frame.bind("<Right>", (lambda e: None))
            frame.bind("<Up>", (lambda e: None))
            frame.bind("<Down>", (lambda e: None))
            frame.bind("<Control-Key-c>", (lambda e: None))
            frame.bind("<Control-Key-v>", (lambda e: None))

        elif access == "W":
            binding_access = frame.bind("<Key>", "pass")
            frame.unbind("<Key>", binding_access)

        frame.bind(self.space_key_binding, self.space_key)
        frame.bind(self.escape_key_binding, self.normal_key)
        for k in self.insert_key_binding:
            frame.bind(k, self.insert_key)
        self.pack()

    def normal_key(self, _):
        """
        escape_key
        """

        self.selected_mode = "NORMAL"
        self.update_mode()
        self.binding_key(self.workframe.active_buffer, access="R")

        self.workframe.active_buffer.insert(tk.END, "")
        self.workframe.active_buffer.config(state=tk.NORMAL)
        self.workframe.active_buffer.focus_set()

    def insert_key(self, _):
        """
        insert_key
        """
        if self.selected_mode == "NORMAL":
            self.selected_mode = "INSERT"
            self.update_mode()
            self.binding_key(self.workframe.active_buffer, access="W")

            self.workframe.active_buffer.insert(tk.END, "")
            self.workframe.active_buffer.config(state=tk.NORMAL)
            self.workframe.active_buffer.focus_set()

        else:
            return

    def space_key(self, event):
        """
        space_key
        """
        if self.selected_mode == "NORMAL":
            self.selected_mode = "SPACE"
            self.update_mode()

            self.workframe.active_buffer.insert(tk.END, "")
            self.workframe.active_buffer.config(state=tk.DISABLED)
            self.spacebar.focus_set()

            print("pressed", repr(event.char))
            print(self.selected_mode, " activated")
        else:
            return


if __name__ == "__main__":

    from workframe import WorkFrame
    from statusbar import StatusBar
    from spacebar import SpaceBar

    ROOT = tk.Tk()

    FRAME_1 = WorkFrame(ROOT)
    FRAME_2 = StatusBar(ROOT)
    FRAME_3 = SpaceBar(ROOT)

    FRAME_1.pack()
    FRAME_2.pack()
    FRAME_3.pack()

    MasterCommand(ROOT, FRAME_1, FRAME_2, FRAME_3)

    ROOT.mainloop()
