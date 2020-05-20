import json
import unittest
import responses

from lotify.client import Client
from urllib.parse import urlencode


class BufferedIOBase:
    def __init__(self, name="example.png"):
        self.name = name


class TestClient(unittest.TestCase):
    def setUp(self):
        self.tested = Client(
            client_id='QxUxF..........i51eITH',
            client_secret='fmtJS3GOVTPn4....................bFcIvJf1jo',
            redirect_uri='http://localhost:5000/notify')
        self.token = '123456789abcdefghidhFeXkIQVjmuI6Oz123456789'
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
                'access_token': self.token
            },
            status=200
        )

        result = self.tested.get_access_token('foo')
        request = responses.calls[0]
        response = json.loads(request.response.content.decode())
        self.assertEqual('POST', request.request.method)
        self.assertEqual(self.token, response.get('access_token'))
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

        result = self.tested.status(self.token)
        request = responses.calls[0]
        response = json.loads(request.response.content.decode())
        self.assertEqual('GET', request.request.method)
        self.assertEqual(200, response.get('status'))
        self.assertEqual(result, expect_response)

    @responses.activate
    def test_send_message(self):
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

        result = self.tested.send_message(
            self.token,
            message='This is notify message'
        )
        request = responses.calls[0]
        response = json.loads(request.response.content.decode())
        self.assertEqual('POST', request.request.method)
        self.assertEqual(200, response.get('status'))
        self.assertEqual(result, expect_response)

    @responses.activate
    def test_send_message_with_sticker(self):
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

        result = self.tested.send_message_with_sticker(
            self.token,
            message='This is notify message',
            sticker_package_id=1,
            sticker_id=1
        )

        request = responses.calls[0]
        response = json.loads(request.response.content.decode())
        self.assertEqual('POST', request.request.method)
        self.assertEqual(200, response.get('status'))
        self.assertEqual(result, expect_response)

    @responses.activate
    def test_send_message_with_image_url(self):
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

        result = self.tested.send_message_with_image_url(
            self.token,
            message='This is notify message',
            image_thumbnail='https://image.com/abc.png',
            image_fullsize='https://image.com/abc.png'
        )

        request = responses.calls[0]
        response = json.loads(request.response.content.decode())
        self.assertEqual('POST', request.request.method)
        self.assertEqual(200, response.get('status'))
        self.assertEqual(result, expect_response)

    @responses.activate
    def test_send_message_with_image_file(self):
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
        result = self.tested.send_message_with_image_file(
            self.token,
            message='This is notify message',
            file='This is file object'
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
