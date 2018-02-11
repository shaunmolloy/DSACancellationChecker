# -*- coding: utf-8 -*-
"""
Browser
Splinter supports javascript and a number of webdrivers
"""
from splinter import Browser
from lib.helpers import helpers

class browser:
    def __init__(self, url = None):
        self.driver = Browser('chrome', headless=True)
        url and self.get(url)

    """
    Get page
    calls Browser.visit
    """
    def get(self, url):
        helpers.message("Connecting to %s" % (url))
        self.driver.visit(url)
        return self
