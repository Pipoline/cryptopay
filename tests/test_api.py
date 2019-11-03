from cryptopay.api import Client


class TestApi():
    api = Client()

    def test_login(self):
        self.api.login()
