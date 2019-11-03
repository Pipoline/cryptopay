"""
Crypto.com API module
"""

import requests


class Client (object):

    headers = {}

    def __init__(self, secret_key=None, api_endpoint_url='https://pay.crypto.com', timeout=30, session=None,
                 ssl_verify=True):
        self.timeout = timeout
        self.req = session or requests
        self.api_endpoint_url = api_endpoint_url
        self.secret_key = secret_key

    def _call_api(self, location, method="GET", **kwargs):
        if method == "GET":
            self.req.get(f'{self.api_endpoint_url}/{location}',
                         headers=self.headers,
                         verify=self.ssl_verify,
                         proxies=self.proxies,
                         timeout=self.timeout
                         )

    def get_payments(self):
        self._call_api()
