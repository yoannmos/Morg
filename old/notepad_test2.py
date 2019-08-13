"""
mod
"""
# import os

# import tkinter
import tkinter.messagebox

from app import ROOT
from command import FileCommand


class Notepad:
    """
    Notepad
    """

    # ROOT = tkinter.Tk()

    # default window width and height
    window_width = 300
    window_height = 300
    text_area = tkinter.Text(ROOT)
    menu_bar = tkinter.Menu(ROOT)
    file_menu = tkinter.Menu(menu_bar, tearoff=0)
    edit_menu = tkinter.Menu(menu_bar, tearoff=0)
    help_menu = tkinter.Menu(menu_bar, tearoff=0)

    # To add scrollbar
    scroll_bar = tkinter.Scrollbar(text_area)
    file_buffer = None

    def __init__(self, **kwargs):
        # super().__init__(self, master=ROOT)

        # Set icon
        try:
            ROOT.wm_iconbitmap("Morg/morgapp/Notepad.ico")
        except ValueError:
            print("No logo found")

        # Set window size (the default is 300x300)

        try:
            self.window_width = kwargs["width"]
        except KeyError:
            pass

        try:
            self.window_height = kwargs["height"]
        except KeyError:
            pass

        # Set the window text
        ROOT.title("Untitled - Notepad")

        # Center the window
        screen_width = ROOT.winfo_screenwidth()
        screen_height = ROOT.winfo_screenheight()
        # For left-alling
        left = (screen_width / 2) - (self.window_width / 2)

        # For right-allign
        top = (screen_height / 2) - (self.window_height / 2)

        # For top and bottom
        ROOT.geometry(
            "%dx%d+%d+%d" % (self.window_width, self.window_height, left, top)
        )

        # To make the textarea auto resizable
        ROOT.grid_rowconfigure(0, weight=1)
        ROOT.grid_columnconfigure(0, weight=1)

        # Add controls (widget)
        self.text_area.grid(sticky=tkinter.N + tkinter.E + tkinter.S + tkinter.W)

        # To open new file
        self.file_menu.add_command(label="New", command=FileCommand.new_file)

        # To open a already existing file
        self.file_menu.add_command(
            label="Open", command=FileCommand.open_file(self.text_area)
        )

        # To save current file
        self.file_menu.add_command(
            label="Save", command=FileCommand.save_file(self.text_area)
        )

        # To create a line in the dialog
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.quit_application)

        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        # To give a feature of cut
        self.edit_menu.add_command(label="Cut", command=self.cut)

        # to give a feature of copy
        self.edit_menu.add_command(label="Copy", command=self.copy)

        # To give a feature of paste
        self.edit_menu.add_command(label="Paste", command=self.paste)

        # To give a feature of editing
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)

        # To create a feature of description of the notepad
        self.help_menu.add_command(label="About Notepad", command=self.show_about)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)

        ROOT.config(menu=self.menu_bar)

        self.scroll_bar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        # Scrollbar will adjust automatically according to the content
        self.scroll_bar.config(command=self.text_area.yview)
        self.text_area.config(yscrollcommand=self.scroll_bar.set)

    def quit_application(self):
        """
        quit
        """
        ROOT.destroy()
        # exit()

    def show_about(self):
        """
        show
        """
        tkinter.messagebox.showinfo("Notepad", "Test")

    def cut(self):
        """
        Cut
        """
        self.text_area.event_generate("<<Cut>>")

    def copy(self):
        """
        Copy
        """
        self.text_area.event_generate("<<Copy>>")

    def paste(self):
        """
        Paste
        """
        self.text_area.event_generate("<<Paste>>")

    def run(self):
        """
        Run main application
        """
        ROOT.mainloop()


# Run main application
NOTEPAD = Notepad(width=600, height=400)

NOTEPAD.run()


# """
# Module doc
# """
# import tkinter
# import tkinter.ttk as ttk


# class Application(tkinter.Frame):
#     """
#     App
#     """

#     def __init__(self, master):
#         tkinter.Frame.__init__(self, master)
#         self.master.minsize(width=800, height=800)
#         self.master.config()
#         app_style = ttk.Style()
#         app_style.theme_use("clam")  # ('clam', 'alt', 'default', 'classic')
#         self.number = 0
#         self.widgets = []
#         self.grid()
#         self.create_widgets()

#     def create_widgets(self):
#         """
#         create widget
#         """
#         self.vertical_button = tkinter.ttk.Button(
#             self, text="vertical", command=self.clone()
#         )
#         self.horizontal_button = tkinter.ttk.Button(
#             self, text="horizontal", command=self.clone()
#         )
#         self.vertical_button.grid(row=0, column=0)
#         self.horizontal_button.grid(row=0, column=1)

#     def clone(self):
#         """
#         clone
#         """
#         buffer = tkinter.ttk.Label(
#             self,
#             text="Buffer #%s" % self.number,
#             borderwidth=2,
#             relief="groove",
#             style="",
#         )

#         buffer.grid(row=10, column=0)
#         self.widgets.append(buffer)
#         self.number += 1


# if __name__ == "__main__":
#     ROOT = tkinter.Tk()
#     ROOT.title("Morg")
#     APP = Application(ROOT)
#     APP.mainloop()

# #         self.master.minsize(width=800, height=800)
# #         self.master.config()
# #         app_style = ttk.Style()
# #         app_style.theme_use("default")  # ('clam', 'alt', 'default', 'classic')

# #         main_window = tkinter.PanedWindow()

# #         main_window.pack(fill=tkinter.BOTH, expand=True)
# #         main_window.configure(background="blue")
# #         paned_button = tkinter.Button(
# #             main_window,
# #             text="Add PanedWindow",
# #             width=25,
# #             command=self.add_window(main_window, tkinter.VERTICAL),
# #         )
# #         paned_button.pack(side=tkinter.LEFT, padx=0, pady=0)
# #         # main_window.add(paned_button)

# #         main_buffer = tkinter.Label(main_window, text="main_buffer")
# #         main_window.add(main_buffer)

# #     def add_window(self, active_window, side):
# #         """
# #         add
# #         """
# #         new_window = tkinter.PanedWindow(active_window, orient=side)  # tkinter.VERTICAL
# #         new_window.configure(background="red")
# #         active_window.add(new_window)

# #         new_buffer = tkinter.Label(new_window, text="new_buffer")
# #         new_window.add(new_buffer)


# # if __name__ == "__main__":
# #     ROOT = tkinter.Tk()
# #     ROOT.title("Morg")
# #     APP = Application(ROOT)
# #     APP.mainloop()


# # # main_window = tkinter.PanedWindow()
# # # main_window.pack(fill=tkinter.BOTH, expand=True)
# # # main_window.configure(background="blue")
# # # paned_button = tkinter.Button(
# # #     main_window,
# # #     text="Add PanedWindow",
# # #     width=25,
# # #     command=add_window(main_window, tkinter.VERTICAL),
# # # )
# # # paned_button.pack(side=tkinter.LEFT, padx=5, pady=5)
# # # main_window.add(paned_button)

# # # main_buffer = tkinter.Label(main_window, text="main_buffer")
# # # main_window.add(main_buffer)


# # # # bottom = tkinter.Label(m2, text="bottom pane")
# # # # m2.add(bottom)

# # # # tkinter.mainloop()
# # # ROOT = tkinter.Tk()
# # # APP = Application(ROOT)
# # # APP.mainloop()


# """
# Module doc
# """
# import tkinter


# class Application(tkinter.Frame):
#     """
#     App
#     """

#     space_key_binding = "<space>"
#     escape_key_binding = "<Escape>"
#     insert_key_binding = [
#         "a",  # Append text following current cursor position
#         "A",  # Append text to the end of current line
#         "i",  # Insert text before the current cursor position
#         "I",  # Insert text at the beginning of the cursor line
#         "o",  # Open up a new line following the current line and add text there
#         "O",  # Open up a new line in front of the current line and add text there
#     ]

#     def __init__(self, master):
#         tkinter.Frame.__init__(self, master)

#         self.master.minsize(width=800, height=800)
#         self.master.config()
#         self.window = tkinter.Text(ROOT, state="normal", width=80, height=24)
#         self.powerbar = tkinter.Text(ROOT, state="normal", width=80, height=4)

#         # -----------------------------------------------------------------------------
#         # MODE Binding

#         self.master.bind(self.space_key_binding, self.space_key)
#         self.master.bind(self.escape_key_binding, self.escape_key)
#         for k in self.insert_key_binding:
#             self.master.bind(k, self.insert_key)
#         # -----------------------------------------------------------------------------
#         self.main_frame = tkinter.Frame()

#         self.selected_mode = "NORMAL"
#         self.set_mode("NORMAL")
#         self.pack()

#     def set_mode(self, mode):
#         """
#         set_mode
#         """
#         if mode == "SPACE":
#             self.selected_mode = "SPACE"
#             self.window["state"] = "disabled"
#             self.powerbar["state"] = "normal"

#         elif mode == "NORMAL":
#             self.selected_mode = "NORMAL"
#             self.window["state"] = "disabled"
#             self.powerbar["state"] = "disabled"

#         elif mode == "INSERT":
#             self.selected_mode = "INSERT"
#             self.window["state"] = "normal"
#             self.powerbar["state"] = "disabled"

#     def space_key(self, event):
#         """
#         space_key
#         """
#         if self.selected_mode == "NORMAL":
#             self.set_mode("SPACE")
#         else:
#             return

#         print("pressed", repr(event.char))
#         print(self.selected_mode, " activated")

#     def escape_key(self, event):
#         """
#         escape_key
#         """
#         self.set_mode("NORMAL")

#         print("pressed", repr(event.char))
#         print(self.selected_mode, " activated")

#     def insert_key(self, event):
#         """
#         insert_key
#         """
#         if self.selected_mode == "NORMAL":
#             self.set_mode("INSERT")

#         print("pressed", repr(event.char))
#         print(self.selected_mode, " activated")


# if __name__ == "__main__":
#     ROOT = tkinter.Tk()
#     APP = Application(ROOT)
#     APP.mainloop()

# # ---------------------------------------------------------------------
# # root = tkinter.Tk()
# # window = tkinter.Text(root, state="normal", width=80, height=24)
# # bar = tkinter.Text(root, state="normal", width=80, height=4)

# # frame = tkinter.Frame(root, width=100, height=100)
