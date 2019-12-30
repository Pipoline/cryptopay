import pytest
import os
from importlib import reload

import cryptopay
from cryptopay.exceptions import ApiKeyMissingException
from requests import Response


@pytest.fixture()
def client():
    from cryptopay import Client
    return Client()


def test_get_payments(client):
    response = client.get_payments()
    assert(isinstance(response, Response))
    assert response.status_code == 200


def test_get_payments(client):
    payment_id = client.get_payments().json()[-1]['id']
    response = client.get_payments(payment_id=payment_id)
    assert(isinstance(response, Response))
    assert response.status_code == 200
