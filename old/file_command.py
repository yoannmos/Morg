# class FileCommand:
#     """
#     Class File Command
#     Simplify File Naming
#     Try to eliminate ROOT use
#     """

#     file_buffer = None

#     def __init__(self, text_area):
#         self.text_area = text_area

#     def open_file(self):
#         """
#         open file
#         """
#         self.file_buffer = tk.filedialog.askopenfilename(
#             defaultextension=".txt",
#             filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")],
#         )

#         if self.file_buffer == "":

#             # no file to open
#             self.file_buffer = None
#         else:

#             # Try to open the file
#             # set the window title
#             # ROOT.title(os.path.basename(self.file_buffer) + " - Notepad") <- Solve ROOT
#             self.text_area.delete(1.0, tk.END)

#             file = open(self.file_buffer, "r")

#             self.text_area.insert(1.0, file.read())

#             file.close()

#     def new_file(self):
#         """
#         new file
#         """
#         # ROOT.title("Untitled - Notepad") <- Solve ROOT
#         self.file_buffer = None
#         self.text_area.delete(1.0, tk.END)

#     def save_file(self):
#         """
#         Save file
#         """
#         if self.file_buffer is None:
#             # Save as new file
#             self.file_buffer = tk.filedialog.asksaveasfilename(
#                 initialfile="Untitled.txt",
#                 defaultextension=".txt",
#                 filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")],
#             )

#             if self.file_buffer == "":
#                 self.file_buffer = None
#             else:

#                 # Try to save the file
#                 file = open(self.file_buffer, "w")
#                 file.write(self.text_area.get(1.0, tk.END))
#                 file.close()

#                 # Change the window title
#                 # ROOT.title(os.path.basename(self.file_buffer) + " - Notepad") <- Solve ROOT

#         else:
#             file = open(self.file_buffer, "w")
#             file.write(self.text_area.get(1.0, tk.END))
#             file.close()


# class ContentCommand:
#     """
#     Class Content Command
#     """

#     def __init__(self, text_area):
#         self.text_area = text_area

#     def cut(self):
#         """
#         Cut
#         """
#         self.text_area.event_generate("<<Cut>>")

#     def copy(self):
#         """
#         Copy
#         """
#         self.text_area.event_generate("<<Copy>>")

#     def paste(self):
#         """
#         Paste
#         """
#         self.text_area.event_generate("<<Paste>>")
