
class Mode:
    """
    """
    
    def __init__(self, name, color, behavior):
        self.name = name
        self.color = color
        self.key = []
        self.behavior = []

    def set_Mode():
        # if key is pressed:
            # find key in selected_mode
        # return mode


class Space_Mode(Mode):

    space = "SPACE"
    color = "black"
    key = ["SPC"]


class Normal_Mode(Mode):

    name = "NORMAL"
    color = "orange"
    key = ["ESC"]

class Insert_Mode(Mode):

    name = "INSERT"
    color = "green"
    key = [
            "a", # Append text following current cursor position
            "A", # Append text to the end of current line
            "i", # Insert text before the current cursor position
            "I", # Insert text at the beginning of the cursor line
            "o", # Open up a new line following the current line and add text there
            "O"  # Open up a new line in front of the current line and add text there
          ]

class Visual_Mode(Mode):
    name = "VISUAL"
    color = "grey"
    key = ["v"]


