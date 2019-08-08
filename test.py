import sys

if sys.version_info[0] < 3:
    import Tkinter as tk
else:
    import tkinter as tk

# Root window
root = tk.Tk()

# Tab override handler
def overrideTab(*args):
    root.bind("<Tab>", stopTab)


def stopTab(event=None, *args):
    if ctrlChk4.get() == 1:
        print("Tab is overridden")
        return "break"
    else:
        print("Tab is not overridden")  # Note that it still prints this.


# Control variable
ctrlChk4 = tk.IntVar()
ctrlChk4.trace("w", overrideTab)

# GUI widgets
fra1 = tk.Frame(root)
chk1 = tk.Checkbutton(fra1, text="First checkbutton")
chk2 = tk.Checkbutton(fra1, text="Second checkbutton")
chk3 = tk.Checkbutton(fra1, text="Third checkbutton")
chk4 = tk.Checkbutton(fra1, text="Tab override", variable=ctrlChk4)

fra1.grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)
chk1.grid(row=0, column=0, sticky=tk.W, padx=(10, 0), pady=(5, 0))
chk2.grid(row=1, column=0, sticky=tk.W, padx=(10, 0), pady=(5, 0))
chk3.grid(row=2, column=0, sticky=tk.W, padx=(10, 0), pady=(5, 0))
chk4.grid(row=3, column=0, sticky=tk.W, padx=(10, 0), pady=(5, 0))

tk.mainloop()
