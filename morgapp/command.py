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
        self.work_frame = workframe
        self.status_bar = statusbar
        self.space_bar = spacebar

        self.keyboard_entry = ""
        self.selected_mode = ""

        self.space_key_binding = SETTINGS["Commande"]["space_key_binding"]
        self.escape_key_binding = SETTINGS["Commande"]["normal_key_binding"]
        self.insert_key_binding = SETTINGS["Commande"]["insert_key_binding"]

        # Set the default mode
        self.normal_key(True)

        self.pack()

    def update_mode(self):
        """ Update mode label """
        self.status_bar.mode["text"] = self.selected_mode
        self.keyboard_entry = "<SPC>"
        self.space_bar.key["text"] = self.keyboard_entry

    def key_chain(self, event):
        """ key chain in space mode"""
        # print(repr(event.char))
        # self.spacebar.key.focus_set()
        # if self.keyboard_entry == "<SPC>":
        #     self.keyboard_entry = ""
        self.keyboard_entry += " "
        self.keyboard_entry += event.char
        self.keyboard_entry += ""
        self.space_bar.key["text"] = self.keyboard_entry

    def binding_key(self, frame):
        """ MODE Binding """
        # TODO: Delete commande character
        # use binding tag and post class binding
        # Exemple in _Module_Exemple

        frame.focus_set()

        if self.selected_mode == "NORMAL":
            frame.bind(self.space_key_binding, self.space_key)
            for k in self.insert_key_binding:
                frame.bind(k, self.insert_key)
            binding_access = frame.bind("<Key>", "pass")
            frame.bind("<Left>", (lambda e: None))
            frame.bind("<Right>", (lambda e: None))
            frame.bind("<Up>", (lambda e: None))
            frame.bind("<Down>", (lambda e: None))
            frame.bind("<Control-Key-c>", (lambda e: None))
            frame.bind("<Control-Key-v>", (lambda e: None))

        elif self.selected_mode == "INSERT":

            frame.bind(self.escape_key_binding, self.normal_key)
            binding_access = frame.bind("<Key>", "pass")
            frame.unbind("<Key>", binding_access)
            # self.work_frame.active_buffer.delete("insert -1 chars", "insert")

        elif self.selected_mode == "SPACE":
            frame.bind(self.escape_key_binding, self.normal_key)
            frame.bind("<Key>", self.key_chain)
            # move the cursor to the previous position
            self.work_frame.active_buffer.mark_set("insert", "insert-1c")

        self.pack()

    def normal_key(self, _):
        """
        escape_key
        """
        self.selected_mode = "NORMAL"
        self.update_mode()
        self.binding_key(self.work_frame.active_buffer)

        self.space_bar.pack_forget()

        self.work_frame.active_buffer.insert(tk.END, "")
        self.work_frame.active_buffer.config(state=tk.NORMAL)

        # self.workframe.active_buffer.focus_set()

    def insert_key(self, _):
        """
        insert_key
        """
        if self.selected_mode == "NORMAL":

            self.selected_mode = "INSERT"
            self.update_mode()
            self.binding_key(self.work_frame.active_buffer)

            self.space_bar.pack_forget()

            self.work_frame.active_buffer.insert(tk.END, "")
            self.work_frame.active_buffer.config(state=tk.NORMAL)
            # self.workframe.active_buffer.focus_set()

        else:
            return

    def space_key(self, _):
        """
        space_key
        """
        if self.selected_mode == "NORMAL":

            # self.work_frame.active_buffer.delete(
            #     len(self.work_frame.active_buffer.get()) - 1
            # )

            self.selected_mode = "SPACE"
            self.update_mode()
            self.binding_key(self.space_bar.key)

            self.space_bar.pack()

            # a = int(len(self.self.work_frame.active_buffer.get()))
            # self.work_frame.active_buffer.delete(a - 1)

            # self.workframe.active_buffer.insert(tk.END, "")
            # self.workframe.active_buffer.config(state=tk.DISABLED)

            # self.spacebar.focus_set()

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
