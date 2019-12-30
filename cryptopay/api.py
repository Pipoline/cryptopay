"""
Crypto.com API module
"""

import json
import requests


class Client(object):
    headers = {}

    def __init__(self, secret_key=None, api_endpoint_url='https://pay.crypto.com/api', timeout=30, session=None,
                 ssl_verify=True, proxies=None):
        self.timeout = timeout
        self.req = session or requests
        self.api_endpoint_url = api_endpoint_url
        self.headers['Authorization'] = f"Bearer {secret_key}"
        self.ssl_verify = ssl_verify
        self.proxies = proxies

    def _call_api(self, location, method="GET", **kwargs):
        if method == "GET":
            return json.loads(self.req.get(f'{self.api_endpoint_url}/{location}',
                                           headers=self.headers,
                                           verify=self.ssl_verify,
                                           proxies=self.proxies,
                                           timeout=self.timeout
                                           ).text)

    def get_payments(self):
        return self._call_api('payments')
