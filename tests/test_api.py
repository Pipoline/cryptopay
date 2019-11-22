from cryptopay.api import Client


class TestApi(object):
    api = Client()

    def test_login(self):
        self.api.login()
