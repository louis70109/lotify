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
            ))

    @responses.activate
    def test_get_access_token(self):
        responses.add(
            responses.POST,
            '{url}/oauth/token'.format(url=self.bot_origin),
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

    @responses.activate
    def test_status(self):
        expect_response = {
            'status': 200,
            'message': 'ok',
            'targetType': 'USER',
            'target': 'NiJia Lin'
        }
        responses.add(
            responses.GET,
            '{url}/api/status'.format(url=self.api_origin),
            json=expect_response,
            status=200
        )

        result = self.tested.status('access_token')
        request = responses.calls[0]
        response = json.loads(request.response.content.decode())
        self.assertEqual('GET', request.request.method)
        self.assertEqual(200, response.get('status'))
        self.assertEqual(result, expect_response)

    @responses.activate
    def test_send(self):
        expect_response = {
            'status': 200,
            'message': 'ok'
        }
        responses.add(
            responses.POST,
            '{url}/api/notify'.format(url=self.api_origin),
            json=expect_response,
            status=200
        )

        result = self.tested.send(
            'access_token',
            params={'message': 'This is notify message'}
        )
        request = responses.calls[0]
        response = json.loads(request.response.content.decode())
        self.assertEqual('POST', request.request.method)
        self.assertEqual(200, response.get('status'))
        self.assertEqual(result, expect_response)

    @responses.activate
    def test_revoke(self):
        expect_response = {
            'status': 200,
            'message': 'ok'
        }
        responses.add(
            responses.POST,
            '{url}/api/revoke'.format(url=self.api_origin),
            json=expect_response,
            status=200
        )

        result = self.tested.revoke('access_token')
        request = responses.calls[0]
        response = json.loads(request.response.content.decode())
        self.assertEqual('POST', request.request.method)
        self.assertEqual(200, response.get('status'))
        self.assertEqual(result, expect_response)
