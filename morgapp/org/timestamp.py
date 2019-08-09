"""
Module Timestamp
"""
from datetime import datetime


class Timestamp:
    """
    Class Timestamp
    """

    def __init__(self):
        self.now = datetime.now()

    def get_date(self):
        """ Fonction get_date """
        return self.now.strftime("[%d-%m-%Y %a]")

    def get_time(self):
        """ Fonction get_time """
        return self.now.strftime("[%H:%M]")

    def get_timestamp(self):
        """ Fonction timestamp """
        return self.now.strftime("[%d-%m-%Y %a %H:%M]")


if __name__ == "__main__":
    T = Timestamp()

    print(T.get_date())
    print(T.get_time())
    print(T.get_timestamp())
