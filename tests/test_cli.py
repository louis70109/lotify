import unittest
import responses
from unittest.mock import patch
from click.testing import CliRunner
from lotify.cli import send_message


class TestCli(unittest.TestCase):
    def setUp(self):
        self.runner = CliRunner()
        self.token = 'YgVGZjHTprZdsooj5xOGXBl9vVwLGBEbjyjaBWY1Mbe'
        self.bot_origin = "https://notify-bot.line.me"
        self.api_origin = "https://notify-api.line.me"

    @responses.activate
    @patch('lotify.client.Client')
    def test_check_status(self, mock_client):
        responses.add(
            responses.GET,
            '{url}/api/status'.format(url=self.api_origin),
            json={
                'status': 200,
                'message': 'ok'
            },
            status=200
        )
        mock_client.status.return_value = {'status': 200, 'message': 'ok'}
        result = self.runner.invoke(send_message, ['--check-status', '--access_token', self.token])
        self.assertEqual(result.output, "Status: {'status': 200, 'message': 'ok'}\n")

    @responses.activate
    @patch('lotify.client.Client')
    def test_send_message(self, mock_client):
        responses.add(
            responses.POST,
            '{url}/api/notify'.format(url=self.api_origin),
            json={
                'status': 200,
                'message': 'ok'
            },
            status=200
        )
        mock_client.send_message.return_value = {'status': 200, 'message': 'ok'}
        result = self.runner.invoke(send_message, ['--access_token', self.token, '--message', 'Hello'])
        self.assertEqual(result.output, "Send notification success.\n")

    @responses.activate
    @patch('lotify.client.Client')
    def test_send_image_with_image_url(self, mock_client):
        responses.add(
            responses.POST,
            '{url}/api/notify'.format(url=self.api_origin),
            json={
                'status': 200,
                'message': 'ok'
            },
            status=200
        )
        mock_client.send_message_with_image_url.return_value = {'status': 200, 'message': 'ok'}
        result = self.runner.invoke(send_message, ['--access_token', self.token, '--message', 'Hello', '--image-url', 'https://example.com/image.png'])
        self.assertEqual(result.output, "Send notification success.\n")

    @responses.activate
    @patch('lotify.client.Client')
    def test_send_image_with_image_file(self, mock_client):
        responses.add(
            responses.POST,
            '{url}/api/notify'.format(url=self.api_origin),
            json={
                'status': 200,
                'message': 'ok'
            },
            status=200
        )

        with self.runner.isolated_filesystem():
            with open('image.png', 'w') as f:
                f.write('This is file object')
            mock_client.send_message_with_image_file.return_value = {'status': 200, 'message': 'ok'}
            result = self.runner.invoke(send_message, ['--access_token', self.token, '--message', 'Hello', '--image-file', 'image.png'])

        self.assertEqual(result.output, "Send notification success.\n")

    @responses.activate
    @patch('lotify.client.Client')
    def test_send_sticker_message(self, mock_client):
        responses.add(
            responses.POST,
            '{url}/api/notify'.format(url=self.api_origin),
            json={
                'status': 200,
                'message': 'ok'
            },
            status=200
        )
        mock_client.send_sticker_message.return_value = {'status': 200, 'message': 'ok'}
        result = self.runner.invoke(send_message, ['--access_token', self.token, '--message', 'Hello', '--sticker-package-id', '1', '--sticker-id', '1'])
        self.assertEqual(result.output, "Send notification success.\n")
