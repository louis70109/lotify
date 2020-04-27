# Lotify - LINE Notify client SDK
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/louis70109/line-notify#contributing)

This is [LINE Notify](https://notify-bot.line.me/doc/en/) client SDK that you can build Notify bot quickly.

# Usage

You need a LINE account and create a Notify like this:
![create-a-line-notify](https://i.imgur.com/m9q4jLO.png)

## initialize instance

```python
from line_notify.client import Client

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


## Send Message

### Just message
![push-notify](https://i.imgur.com/RhvwZVm.png)

```python
response = client.send(access_token='YOUR_ACCESS_TOKEN', params={
    'message': 'This is notify message'
})
print(response)
# {'status': 200, 'message': 'ok'}
```

![push-notify-with-sticker](https://i.imgur.com/EWpZahk.png)


### With sticker, image_path, thumbnail or fullsize image
You can find stickerId and stickerPackageId [here](https://devdocs.line.me/files/sticker_list.pdf) 
```python
# push message with sticker or image
response = client.send(access_token='YOUR_ACCESS_TOKEN', params={
    'message': 'This is notify message',
    'stickerPackageId': '1',
    'stickerId': '1',
    # image_path='./test_image.png',
    # image_thumbnail='https://i.imgur.com/RhvwZVm.png',
    # image_fullsize='https://i.imgur.com/RhvwZVm.png',
})
print(response)
# {'status': 200, 'message': 'ok'}
```

## Revoke access token
![revoke-line-notify-token](https://i.imgur.com/7GAAzOi.png)

```python
from line_notify.client import Client

client = Client()
revoke = client.revoke(access_token='CKmvd81Yfd9Xv38ayQdt7JN4H90oQrP6srFmKckx3sL')
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
python -m pytest tests/ 
```
# License
[MIT License](https://github.com/louis70109/line-notify/blob/master/LICENSE)