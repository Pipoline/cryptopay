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
        data = kwargs.get('data')

        if method == "GET":
            return session.get(f'{self.api_endpoint_url}/{location}',
                               verify=self.ssl_verify,
                               proxies=self.proxies,
                               timeout=self.timeout
                               )
        elif method == "POST":
            return session.post(f'{self.api_endpoint_url}/{location}',
                                json=data,
                                verify=self.ssl_verify,
                                proxies=self.proxies,
                                timeout=self.timeout
                                )

    def get_payments(self):
        """
        Get all payments
        """
        return self._call_api('payments')

    def get_payment(self, payment_id):
        """
        Get specific payment
        :param payment_id: Payment ID
        """
        return self._call_api(f'payments/{payment_id}')

    def create_payment(self, currency, amount, customer_id=None, description=None, metadata={}, order_id=None):
        """
        Create payment
        """
        data = dict(
            currency=currency,
            amount=amount,
            customer_id=customer_id,
            description=description,
            metadata=metadata,
            order_id=order_id
        )
        return self._call_api('payments', method='POST', data=data)

    def cancel_payment(self, payment_id):
        """
        Cancel payment
        """
        return self._call_api(f'payments/{payment_id}/cancel', method='POST')

    def list_refunds(self, payment_id):
        """
        List refunds for payment
        """
        return self._call_api(f'refunds/{payment_id}')

    def request_refund(self, payment_id, amount, reason="", description=""):
        """
        Request refund for payment
        """
        data = dict(
            payment_id=payment_id,
            amount=amount,
            reason=reason,
            description=description
        )
        return self._call_api(f'refunds', method='POST', data=data)

