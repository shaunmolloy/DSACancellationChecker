"""
Captcha
"""
from subprocess import call
import os
import urllib.request

class captcha:
    def __init__(self):
        self.filename = "cache/captcha.jpeg"

    """
    Download image
    """
    def download_image(self, url):
        urllib.request.urlretrieve(url, self.filename)

    """
    Show image in terminal
    """
    def show_image(self):
        # TODO fallback to PIL.Image open/show
        print("\n")
        call(["./lib/imgcat", self.filename])
        print("\n\n\n")

    """
    Delete image
    """
    def delete_image(self):
        os.remove(self.filename)
