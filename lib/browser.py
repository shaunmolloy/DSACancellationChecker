# -*- coding: utf-8 -*-
"""
Browser
Splinter supports javascript and a number of webdrivers
"""
from splinter import Browser
from datetime import datetime

class browser:
    def __init__(self, url = None):
        self.driver = Browser('chrome', headless=True)
        url and self.get(url)

    def get_time(self):
        return datetime.now().strftime("%X")

    """
    Get page
    calls Browser.visit
    """
    def get(self, url):
        print("[%s] Connecting to %s" % (
            self.get_time(),
            url
        ) )
        self.driver.visit(url)
        return self
