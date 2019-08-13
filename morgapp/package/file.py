"""
File Module
"""

from __master import BufferMenu

COMPATIBILITY = ".ALL"


class FileMenu(BufferMenu):
    """ File Menu """

    def __init__(self):
        super().__init__()
        self.title = "File"
        self.key = "f"
        self.add_option("Open", "o", self.open_file)
        self.add_option("Save", "s", self.save_file)
        self.add_option("Save As...", "S", self.save_file)

    def open_file(self):
        """
        Open file
        """
        return print("File Opened")

    def save_file(self):
        """
        Save file
        """
        return print("File Saved")


if __name__ == "__main__":

    MB = FileMenu()
    MB.set_layout()
    MB.print_layout()
