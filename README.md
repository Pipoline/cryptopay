# cryptopay
Python API wrapper for [Crypto.com Pay Checkout](https://pay-docs.crypto.com)

![Travis (.com)](https://img.shields.io/travis/com/pipoline/cryptopay) ![Codecov](https://img.shields.io/codecov/c/github/pipoline/cryptopay) ![PyPI - Downloads](https://img.shields.io/pypi/dm/cryptopay) ![PyPI](https://img.shields.io/pypi/v/cryptopay)
### Installation
- From pypi:
`pip3 install cryptopay`
- From GitHub:
Clone our repository and `python3 setup.py install`

### Usage
```python
from pprint import pprint
from cryptopay import Client

client = Client()
response = client.get_payments()
payments = response.json()
pprint(payments)
```
