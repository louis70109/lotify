Lotify - LINE Notify client SDK
===============================

|License: MIT| |PRs Welcome|

**Lotify** is a `LINE Notify`_ client SDK that you can build Notify bot
quickly.

Usage
=====

   Version suggest >= 3.7

You need a **LINE account** and create a Notify like this:

.. figure:: https://i.imgur.com/m9q4jLO.png
   :alt: create-a-line-notify

   create-a-line-notify

Install package
---------------

``shell script pip install lotify``

initialize instance
-------------------

.. code:: python

   from lotify.client import Client

   client = Client(
       client_id='YOUR_CLIENT_ID',
       client_secret='YOUR_CLIENT_SECRET',
       redirect_uri='YOUR_URI'
   )

Get authorizer link
-------------------

.. code:: python

   link = client.get_auth_link(state='RANDOM_STRING')
   print(link)
   # https://notify-bot.line.me/oauth/authorize?scope=notify&response_type=code&client_id=QxUxF..........i51eITH&redirect_uri=http%3A%2F%2Flocalhost%3A5000%2Fnotify&state=foo

Get access token
----------------

.. code:: python

   access_token = client.get_access_token(code='NOTIFY_RESPONSE_CODE')
   print(access_token)
   # N6g50DiQZk5Xh...25FoFzrs2npkU3z

Get Status
----------

.. code:: python

   status = client.status(access_token='YOUR_ACCESS_TOKEN')
   print(status)
   # {'status': 200, 'message': 'ok', 'targetType': 'USER', 'target': 'NiJia Lin'}

Send message
------------

.. figure:: https://i.imgur.com/RhvwZVm.png
   :alt: push-notify

   push-notify

.. code:: python

   response = client.send(access_token='YOUR_ACCESS_TOKEN', params={
       'message': 'This is notify message'
   })
   print(response)
   # {'status': 200, 'message': 'ok'}

Send message with Sticker
-------------------------

.. figure:: https://i.imgur.com/EWpZahk.png
   :alt: push-notify-with-sticker

   push-notify-with-sticker

You can find stickerId and stickerPackageId `here`_

.. code:: python

   # push message with sticker or image
   response = client.send(access_token='YOUR_ACCESS_TOKEN', message='This is notify message')
   print(response)
   # {'status': 200, 'message': 'ok'}

Send message with Image path
----------------------------

.. figure:: https://i.imgur.com/ESCrk8b.png
   :alt: send-message-with-image-path

   send-message-with-image-path

.. code:: python

   from lotify.client import Client

   client = Client()
   image = client.send_message_with_image_path(
       access_token='YOUR_ACCESS_TOKEN',
       message='This is notify message',
       image_path='./test_image.png'
   )
   print(image)
   # {'status': 200, 'message': 'ok'}

Send message with Image url
---------------------------

.. figure:: https://i.imgur.com/0Lxatu9.png
   :alt: send-message-with-image-url

   send-message-with-image-url

.. code:: python

   from lotify.client import Client

   client = Client()
   image = client.send_message_with_image_url(
       access_token='YOUR_ACCESS_TOKEN',
       message='This is notify message',
       image_thumbnail='https://i.imgur.com/RhvwZVm.png',
       image_fullsize='https://i.imgur.com/RhvwZVm.png',
   )
   print(image)
   # {'status': 200, 'message': 'ok'}

Revoke access token
-------------------

.. figure:: https://i.imgur.com/7GAAzOi.png
   :alt: revoke-line-notify-token

   revoke-line-notify-token

\```python client = Client() revoke = client.revoke(access_token=’

.. _LINE Notify: https://notify-bot.line.me/doc/en/
.. _here: https://devdocs.line.me/files/sticker_list.pdf

.. |License: MIT| image:: https://img.shields.io/badge/License-MIT-blue.svg
   :target: https://opensource.org/licenses/MIT
.. |PRs Welcome| image:: https://img.shields.io/badge/PRs-welcome-brightgreen.svg
   :target: https://github.com/louis70109/line-notify#contributing