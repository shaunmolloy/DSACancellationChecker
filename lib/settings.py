import os
from os.path import join, dirname
from dotenv import load_dotenv
import json

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

"""
Vars from .env below
"""
LICENCE = os.environ.get("LICENCE")
APPLICATION_REFERENCE = os.environ.get("APPLICATION_REFERENCE")

EMAILS = json.loads(os.environ.get("EMAILS"))
EMAIL_SERVER_URL = os.environ.get("EMAIL_SERVER_URL")
EMAIL_SERVER_USERNAME = os.environ.get("EMAIL_SERVER_USERNAME")
EMAIL_SERVER_PASSWORD = os.environ.get("EMAIL_SERVER_PASSWORD")

TEST_DATE = os.environ.get("TEST_DATE")
