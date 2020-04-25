import unittest
from line_notify.client import Client


class TestClient(unittest.TestCase):
    def test_get_auth_link(self):

        client = Client(client_id='QxUxF..........i51eITH', client_secret='fmtJS3GOVTPn4....................bFcIvJf1jo',
                        redirect_uri='http://localhost:5000/notify')
        result = client.get_auth_link('foo')
        self.assertEqual(result, 'https://notify-bot.line.me/oauth/authorize?scope=notify&response_type=code&client_id=QxUxF..........i51eITH&redirect_uri=http%3A%2F%2Flocalhost%3A5000%2Fnotify&state=foo')
