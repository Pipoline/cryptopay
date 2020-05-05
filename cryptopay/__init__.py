"""
Crypto.com pay wrapper library
"""
import os
import requests
from .exceptions import ApiKeyMissingException

CRYPTOPAY_SECRET_KEY = os.environ.get('CRYPTOPAY_SECRET_KEY', None)

session = requests.Session()
session.headers['Authorization'] = f"Bearer {CRYPTOPAY_SECRET_KEY}"

from .api import Client
