"""
This file contains all the configuration settings, including your Nexmo API key, API secret, and other relevant settings.
"""
import os

from dotenv import load_dotenv

load_dotenv(".env.development")

NEXMO_API_KEY = os.environ["NEXMO_API_KEY"]
NEXMO_API_SECRET = os.environ["NEXMO_API_SECRET"]
FROM_PHONE_NUMBER = os.environ["FROM_PHONE_NUMBER"]
TO_PHONE_NUMBER = os.environ["TO_PHONE_NUMBER"]
