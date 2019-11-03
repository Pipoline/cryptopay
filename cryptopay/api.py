"""
Crypto.com API module
"""


class Client (object):

    endpoint = 'https://pay.crypto.com'
    settings = {}

    def __init__(self, settings=None):
        self.settings = settings

    def login(self):
        pass
