"""
Module doc
"""
import tkinter
import tkinter.ttk as ttk


class Application(tkinter.Frame):
    """
    App
    """

    def __init__(self, master):
        tkinter.Frame.__init__(self, master)
        self.master.minsize(width=800, height=800)
        self.master.config()
        app_style = ttk.Style()
        app_style.theme_use("clam")  # ('clam', 'alt', 'default', 'classic')
        self.number = 0
        self.widgets = []
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """
        create widget
        """
        self.vertical_button = tkinter.ttk.Button(
            self, text="vertical", command=self.clone()
        )
        self.horizontal_button = tkinter.ttk.Button(
            self, text="horizontal", command=self.clone()
        )
        self.vertical_button.grid(row=0, column=0)
        self.horizontal_button.grid(row=0, column=1)

    def clone(self):
        """
        clone
        """
        buffer = tkinter.ttk.Label(
            self,
            text="Buffer #%s" % self.number,
            borderwidth=2,
            relief="groove",
            style="",
        )

        buffer.grid(row=10, column=0)
        self.widgets.append(buffer)
        self.number += 1


if __name__ == "__main__":
    ROOT = tkinter.Tk()
    ROOT.title("Morg")
    APP = Application(ROOT)
    APP.mainloop()

#         self.master.minsize(width=800, height=800)
#         self.master.config()
#         app_style = ttk.Style()
#         app_style.theme_use("default")  # ('clam', 'alt', 'default', 'classic')

#         main_window = tkinter.PanedWindow()

#         main_window.pack(fill=tkinter.BOTH, expand=True)
#         main_window.configure(background="blue")
#         paned_button = tkinter.Button(
#             main_window,
#             text="Add PanedWindow",
#             width=25,
#             command=self.add_window(main_window, tkinter.VERTICAL),
#         )
#         paned_button.pack(side=tkinter.LEFT, padx=0, pady=0)
#         # main_window.add(paned_button)

#         main_buffer = tkinter.Label(main_window, text="main_buffer")
#         main_window.add(main_buffer)

#     def add_window(self, active_window, side):
#         """
#         add
#         """
#         new_window = tkinter.PanedWindow(active_window, orient=side)  # tkinter.VERTICAL
#         new_window.configure(background="red")
#         active_window.add(new_window)

#         new_buffer = tkinter.Label(new_window, text="new_buffer")
#         new_window.add(new_buffer)


# if __name__ == "__main__":
#     ROOT = tkinter.Tk()
#     ROOT.title("Morg")
#     APP = Application(ROOT)
#     APP.mainloop()


# # main_window = tkinter.PanedWindow()
# # main_window.pack(fill=tkinter.BOTH, expand=True)
# # main_window.configure(background="blue")
# # paned_button = tkinter.Button(
# #     main_window,
# #     text="Add PanedWindow",
# #     width=25,
# #     command=add_window(main_window, tkinter.VERTICAL),
# # )
# # paned_button.pack(side=tkinter.LEFT, padx=5, pady=5)
# # main_window.add(paned_button)

# # main_buffer = tkinter.Label(main_window, text="main_buffer")
# # main_window.add(main_buffer)


# # # bottom = tkinter.Label(m2, text="bottom pane")
# # # m2.add(bottom)

# # # tkinter.mainloop()
# # ROOT = tkinter.Tk()
# # APP = Application(ROOT)
# # APP.mainloop()
