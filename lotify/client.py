# -*- coding: utf-8 -*-
import os

import requests
from urllib.parse import urlencode


class Client:
    CLIENT_ID = os.environ.get('LINE_NOTIFY_CLIENT_ID')
    CLIENT_SECRET = os.environ.get('LINE_NOTIFY_CLIENT_SECRET')
    REDIRECT_URI = os.environ.get('LINE_NOTIFY_REDIRECT_URI')

    def __init__(self,
                 client_id=None,
                 client_secret=None,
                 redirect_uri=None,
                 bot_origin=None,
                 api_origin=None,
                 *args, **kwargs):
        self.client_id = client_id or self.CLIENT_ID
        self.client_secret = client_secret or self.CLIENT_SECRET
        self.redirect_uri = redirect_uri or self.REDIRECT_URI

        self.bot_origin = bot_origin or "https://notify-bot.line.me"
        self.api_origin = api_origin or "https://notify-api.line.me"

    def __repr__(self):
        return f"<Lotify client_id={self.client_id}, client_secret={self.client_secret}, " \
               f"redirect_uri={self.redirect_uri}, bot_origin={self.bot_origin}, " \
               f"api_origin={self.api_origin}>"

    def get_auth_link(self, state,form_post=False):
        query_string = {
            'scope': 'notify',
            'response_type': 'code',
            'client_id': self.client_id,
            'redirect_uri': self.redirect_uri,
            'state': state
        }
        if form_post:query_string.update({'response_mode':'form_post'})
        return '{url}/oauth/authorize?{query_string}'.format(
            url=self.bot_origin, query_string=urlencode(query_string))

    def get_access_token(self, code):
        response = self._post(
            url='{url}/oauth/token'.format(url=self.bot_origin),
            headers={
                'Content-Type': 'application/x-www-form-urlencoded',
            }, data={
                'grant_type': 'authorization_code',
                'code': code,
                'redirect_uri': self.redirect_uri,
                'client_id': self.client_id,
                'client_secret': self.client_secret
            })
        return response.json().get('access_token')

    def status(self, access_token):
        response = self._get(
            url='{url}/api/status'.format(url=self.api_origin),
            headers={
                'Content-Type': 'application/x-www-form-urlencoded',
                'Authorization': 'Bearer {token}'.format(token=access_token)
            })
        return response.json()

    def send_message(self, access_token, message, notification_disabled=False):
        params = {'message': message}
        if notification_disabled:
            params.update({'notificationDisabled': notification_disabled})

        response = self._post(
            url='{url}/api/notify'.format(url=self.api_origin),
            data=params,
            headers={
                'Authorization': 'Bearer {token}'.format(token=access_token)
            })
        return response.json()

    def send_message_with_sticker(
            self,
            access_token,
            message,
            sticker_id,
            sticker_package_id,
            notification_disabled=False):
        params = {
            'message': message,
            'stickerPackageId': sticker_package_id,
            'stickerId': sticker_id
        }
        if notification_disabled:
            params.update({'notificationDisabled': notification_disabled})

        response = self._post(
            url='{url}/api/notify'.format(url=self.api_origin),
            data=params,
            headers={
                'Authorization': 'Bearer {token}'.format(token=access_token),
                'Content-Type': 'application/x-www-form-urlencoded'
            })
        return response.json()

    def send_message_with_image_url(
            self,
            access_token,
            message,
            image_thumbnail,
            image_fullsize,
            notification_disabled=False):

        params = {
            'message': message,
            'imageFullsize': image_fullsize,
            'imageThumbnail': image_thumbnail
        }
        if notification_disabled:
            params.update({'notificationDisabled': notification_disabled})

        response = self._post(
            url='{url}/api/notify'.format(url=self.api_origin),
            data=params,
            headers={
                'Authorization': 'Bearer {token}'.format(token=access_token)
            })
        return response.json()

    def send_message_with_image_file(
            self,
            access_token,
            message,
            file,
            notification_disabled=False):
        params = {'message': message}

        if notification_disabled:
            params.update({'notificationDisabled': notification_disabled})

        response = self._post(
            url='{url}/api/notify'.format(url=self.api_origin),
            data=params,
            files={'imageFile': file},
            headers={
                'Authorization': 'Bearer {token}'.format(token=access_token)
            })
        return response.json()

    def revoke(self, access_token):
        response = self._post(
            url='{url}/api/revoke'.format(url=self.api_origin),
            headers={
                'Content-Type': 'application/x-www-form-urlencoded',
                'Authorization': 'Bearer {token}'.format(token=access_token)
            })
        return response.json()

    def _get(self, url, headers=None, timeout=1):
        try:
            response = requests.get(url, headers=headers, timeout=timeout)
            self.__check_http_response_status(response)
            return response
        except requests.exceptions.Timeout:
            raise RuntimeError(
                'Request time {timeout} timeout. Please check internet.'.format(timeout=timeout)
            )
        except requests.exceptions.TooManyRedirects:
            raise RuntimeError('URL {url} was bad, please try a different one.'.format(url=url))

    def _post(self, url, data=None, headers=None, files=None, timeout=None):
        try:
            response = requests.post(
                url, headers=headers, data=data, files=files, timeout=timeout)
            self.__check_http_response_status(response)
            return response
        except requests.exceptions.Timeout:
            raise RuntimeError(
                'Request time {timeout} timeout. Please check internet.'.format(timeout=timeout)
            )
        except requests.exceptions.TooManyRedirects:
            raise RuntimeError('URL {url} was bad, please try a different one.'.format(url=url))

    @staticmethod
    def __check_http_response_status(response):
        if 200 <= response.status_code < 300:
            pass
        else:
            raise ValueError(response.json())
