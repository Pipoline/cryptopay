"""
Crypto.com API module
"""

from . import session


class Client:
    headers = {}

    def __init__(self, secret_key=None, api_endpoint_url='https://pay.crypto.com/api', timeout=30,
                 ssl_verify=True, proxies=None):
        self.timeout = timeout
        self.api_endpoint_url = api_endpoint_url
        self.ssl_verify = ssl_verify
        self.proxies = proxies
        if secret_key:
            session.headers['Authorization'] = f"Bearer {secret_key}"

    def _call_api(self, location, method="GET", **kwargs):
        if method == "GET":
            return session.get(f'{self.api_endpoint_url}/{location}',
                               verify=self.ssl_verify,
                               proxies=self.proxies,
                               timeout=self.timeout
                               )

    def get_payments(self):
        return self._call_api('payments')
