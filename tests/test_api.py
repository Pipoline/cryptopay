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


def test_create_payment(client):
    currency = 'EUR'
    amount = 1000  # it's $10
    response = client.create_payment(currency, amount,
                                     description='Testing payment',
                                     order_id=111,
                                     metadata={
                                         "customer_name": "testing customer"
                                     })
    assert response.status_code == 200


def test_get_payments(client):
    payment_id = client.get_payments().json()['items'][-1]['id']
    response = client.get_payment(payment_id)
    assert(isinstance(response, Response))
    assert response.status_code == 200


def test_cancel_payment(client):
    payment_id = client.create_payment('EUR', 2000).json()['id']
    response = client.cancel_payment(payment_id)
    assert (isinstance(response, Response))
    assert response.status_code == 200


def test_list_refunds(client):
    payment_id = client.create_payment('EUR', 2000).json()['id']
    refund_id = client.request_refund(payment_id, 2000)
    response = client.list_refunds(refund_id)

