import pytest
from cryptopay.api import Client
from requests import Response


@pytest.fixture()
def client():
    return Client()


def test_get_payments(client):
    response = client.get_payments()
    assert(isinstance(response, Response))

