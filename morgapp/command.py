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

        self.selected_mode = "NORMAL"
        # self.normal_key()

        self.space_key_binding = SETTINGS["Commande"]["space_key_binding"]
        self.escape_key_binding = SETTINGS["Commande"]["normal_key_binding"]
        self.insert_key_binding = SETTINGS["Commande"]["insert_key_binding"]

        self.update_mode()

        self.status_bar.set_mode(self.selected_mode)
        self.binding_key()
        self.pack()
        # self.spacebar.pack_forget()

    def binding_key(self):
        # MODE Binding
        self.root.bind(self.space_key_binding, self.space_key)
        self.root.bind(self.escape_key_binding, self.normal_key)
        for k in self.insert_key_binding:
            self.root.bind(k, self.insert_key(True))

    def enable_disable(self, frame, status):
        """Enable or Disable a frame"""
        child_list = frame.winfo_children()
        for child in child_list:
            if status == "disable":
                try:
                    frame.configure(state="disable")
                except tk.TclError:
                    try:
                        child.configure(state="disabled")
                    except tk.TclError:
                        pass
            elif status == "normal" or "enable":
                try:
                    frame.configure(state="normal")
                except tk.TclError:
                    child.configure(state="normal")
            else:
                raise ValueError("Wrong status input")

    def update_mode(self):
        """
        Update mode label
        """
        # TODO : Adapt to real status bar, MODE label
        self.status_bar.mode["text"] = self.selected_mode

    def space_key(self, _):
        """
        space_key
        """
        if self.selected_mode == "NORMAL":
            self.selected_mode = "SPACE"
            # self.enable_disable(self.workframe, "disable")
            self.spacebar.pack()
            self.spacebar.focus_set()
            self.update_mode()
        else:
            return

    def normal_key(self, _):
        """
        escape_key
        """
        self.selected_mode = "NORMAL"
        self.update_mode()
        self.spacebar.pack_forget()
        self.workframe.active_buffer.focus_set()
        self.workframe.read_only()
        self.binding_key()

    def insert_key(self, _):
        """
        insert_key
        """
        if self.selected_mode == "NORMAL":
            self.selected_mode = "INSERT"
            self.update_mode()
            # self.enable_disable(self.workframe, "normal")
            self.spacebar.pack_forget()
            self.workframe.active_buffer.focus_set()
            self.workframe.set_normal()

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
