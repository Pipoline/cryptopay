"""
Crypto.com API module
"""
import requests


class Client (object):

    endpoint = 'https://pay.crypto.com'
    settings = {"token": ""}
    session = None

    def __init__(self, settings=settings):
        self.settings = settings
        self.session = requests.Session()
        self.login()

    def login(self):
        self.session.headers['Authorization'] = f"Bearer {self.settings.get('token')}"

    def __call_api(self, method, action, **kwargs):
        if method == "post":
            response = self.session.post(f"{self.endpoint}{action}")
        elif method == "get":
            response = self.session.get(f"{self.endpoint}{action}")

    def create_payment(self):
        pass

    def get_payments(self):
        pass

    def cancel_payment(self, id):
        pass


