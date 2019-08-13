"""
Module Menu
"""


class BufferMenu:
    """ Buffer Menu """

    def __init__(self):
        self.title = ""
        self.key = ""
        self.options = []
        self.layout = self.set_layout()

    def set_layout(self):
        """ set menu layout"""
        self.layout = "[{1}] {0}".format(self.title, self.key)
        self.layout += "\n---------"
        for o in self.options:

            self.layout += "\n[{1}] {0}".format(o[0], o[1])
        return self.layout

    def add_option(self, title, key, function):
        """ add an menu option """
        option = []
        option.append(title)
        option.append(key)
        option.append(function)
        self.options.append(option)

    def print_layout(self):
        """ set menu layout"""
        return print(self.layout)


if __name__ == "__main__":

    MB = BufferMenu()
    MB.set_layout()
