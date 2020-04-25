import json
import unittest
import responses

from line_notify.client import Client


class TestClient(unittest.TestCase):
    def test_get_auth_link(self):

        client = Client(client_id='QxUxF..........i51eITH', client_secret='fmtJS3GOVTPn4....................bFcIvJf1jo',
                        redirect_uri='http://localhost:5000/notify')
        result = client.get_auth_link('foo')
        self.assertEqual(result, 'https://notify-bot.line.me/oauth/authorize?scope=notify&response_type=code&client_id=QxUxF..........i51eITH&redirect_uri=http%3A%2F%2Flocalhost%3A5000%2Fnotify&state=foo')

    @responses.activate
    def test_get_access_token(self):
        responses.add(
            responses.POST,
            'https://notify-bot.line.me/oauth/token',
            json={
                'access_token': 'access_token_foo'
            },
            status=200
        )

        client = Client(client_id='QxUxF..........i51eITH', client_secret='fmtJS3GOVTPn4....................bFcIvJf1jo',
                        redirect_uri='http://localhost:5000/notify')
        result = client.get_access_token('foo')
        request = responses.calls[0]
        response = json.loads(responses.calls[0].response.content.decode())
        self.assertEqual('POST', request.request.method)
        self.assertEqual('access_token_foo', response.get('access_token'))
        self.assertEqual(result, response.get('access_token'))


