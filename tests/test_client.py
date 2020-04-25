import json
import unittest
import responses

from line_notify.client import Client
from urllib.parse import urlencode


class TestClient(unittest.TestCase):
    def setUp(self):
        self.tested = Client(
            client_id='QxUxF..........i51eITH',
            client_secret='fmtJS3GOVTPn4....................bFcIvJf1jo',
            redirect_uri='http://localhost:5000/notify')

        self.bot_origin = "https://notify-bot.line.me"
        self.api_origin = "https://notify-api.line.me"

    def test_get_auth_link(self):
        result = self.tested.get_auth_link('foo')
        expected_query_string = {
            'scope': 'notify',
            'response_type': 'code',
            'client_id': 'QxUxF..........i51eITH',
            'redirect_uri': 'http://localhost:5000/notify',
            'state': 'foo'
        }
        self.assertEqual(
            result,
            '{url}/oauth/authorize?{query_string}'.format(
                url=self.bot_origin,
                query_string=urlencode(expected_query_string)
            )
        )

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

        result = self.tested.get_access_token('foo')
        request = responses.calls[0].request
        self.assertEqual('POST', request.method)
        self.assertEqual('access_token_foo', result)

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

        result = self.tested.get_access_token('foo')
        request = responses.calls[0]
        response = json.loads(request.response.content.decode())
        self.assertEqual('POST', request.request.method)
        self.assertEqual('access_token_foo', response.get('access_token'))
        self.assertEqual(result, response.get('access_token'))


