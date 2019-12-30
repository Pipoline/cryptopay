import os
from importlib import reload

import cryptopay
from cryptopay.exceptions import ApiKeyMissingException


def test_missing_api_key():
    tmp = os.environ['CRYPTOPAY_SECRET_KEY']
    del os.environ['CRYPTOPAY_SECRET_KEY']
    try:
        reload(cryptopay)
    except ApiKeyMissingException:
        pass

    os.environ['CRYPTOPAY_SECRET_KEY'] = tmp
    reload(cryptopay)


def test_custom_secret_key():
    client = cryptopay.Client('custom_secret_key')
    assert client



