# Lotify - LINE Notify client SDK

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/louis70109/line-notify#contributing)

**Lotify** is a [LINE Notify](https://notify-bot.line.me/doc/en/) client SDK that you can build Notify bot quickly.

# Usage

> Version suggest >= 3.7

You need a **LINE account** and create a Notify like this:

![create-a-line-notify](https://i.imgur.com/m9q4jLO.png)

## Install package

```shell script
pip install lotify
```

## initialize instance

```python
from lotify.client import Client

client = Client(
    client_id='YOUR_CLIENT_ID',
    client_secret='YOUR_CLIENT_SECRET',
    redirect_uri='YOUR_URI'
)
```

## Get authorizer link

```python
link = client.get_auth_link(state='RANDOM_STRING')
print(link)
# https://notify-bot.line.me/oauth/authorize?scope=notify&response_type=code&client_id=QxUxF..........i51eITH&redirect_uri=http%3A%2F%2Flocalhost%3A5000%2Fnotify&state=foo
```

## Get access token

```python
access_token = client.get_access_token(code='NOTIFY_RESPONSE_CODE')
print(access_token)
# N6g50DiQZk5Xh...25FoFzrs2npkU3z
```

## Get Status
```python
status = client.status(access_token='YOUR_ACCESS_TOKEN')
print(status)
# {'status': 200, 'message': 'ok', 'targetType': 'USER', 'target': 'NiJia Lin'}
```


## Send message

![push-notify](https://i.imgur.com/RhvwZVm.png)

```python
response = client.send(access_token='YOUR_ACCESS_TOKEN', params={
    'message': 'This is notify message'
})
print(response)
# {'status': 200, 'message': 'ok'}
```

## Send message with Sticker

![push-notify-with-sticker](https://i.imgur.com/EWpZahk.png)

You can find stickerId and stickerPackageId [here](https://devdocs.line.me/files/sticker_list.pdf)
 
```python
# push message with sticker or image
response = client.send(access_token='YOUR_ACCESS_TOKEN', message='This is notify message')
print(response)
# {'status': 200, 'message': 'ok'}
```

## Send message with Image path

![send-message-with-image-path](https://i.imgur.com/ESCrk8b.png)

```python
from lotify.client import Client

client = Client()
image = client.send_message_with_image_path(
    access_token='YOUR_ACCESS_TOKEN',
    message='This is notify message',
    image_path='./test_image.png'
)
print(image)
# {'status': 200, 'message': 'ok'}
```

## Send message with Image url

![send-message-with-image-url](https://i.imgur.com/0Lxatu9.png)

```python
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
```

## Revoke access token
![revoke-line-notify-token](https://i.imgur.com/7GAAzOi.png)

```python
client = Client()
revoke = client.revoke(access_token='YOUR_ACCESS_TOKEN')
print(revoke)
# {'status': 200, 'message': 'ok'}
```

# Contributing

Fork before Clone the repository:
```shell script
git clone git@github.com:your-username/line-notify.git
```

Run `pytest` to make sure the tests pass:

```shell script
cd line-notify/
python -m pytest --flake8 tests/ 
```

> If you fix `README` by markdown, you can use [Online Converter](https://pandoc.org/try/) to format to reStructuredText (RST) and run `make check` to valid README🙂.

# License
[MIT ](https://github.com/louis70109/line-notify/blob/master/LICENSE) © [NiJia Lin](https://nijialin.com/about/) & Duncan Huang