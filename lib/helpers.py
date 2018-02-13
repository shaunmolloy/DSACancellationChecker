"""
Helpers
"""
from datetime import datetime

class helpers:
    @staticmethod
    def get_time():
        # eg. Sun 11 Feb 20:00:00
        # see: http://www.geezer.org/sw/mvform/doc/strftime.txt
        return datetime.now().strftime("%a %d %b %X")

    @staticmethod
    def message(message):
        # eg. [Sun 11 Feb 20:00:00] message
        # see: https://stackoverflow.com/questions/5947742/how-to-change-the-output-color-of-echo-in-linux
        print(
            "%s[%s]%s" % ("\033[38;5;028m", helpers.get_time(), "\033[0m"),
            message
        )

    @staticmethod
    def error(message):
        # eg. [Sun 11 Feb 20:00:00] exception
        # see: self.message
        print(
            "%s[%s]%s" % ("\033[38;5;028m", helpers.get_time(), "\033[0m"),
            "%s%s%s" % ("\033[38;5;200m", message, "\033[0m")
        )
