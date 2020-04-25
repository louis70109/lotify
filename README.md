# Introduction 
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/louis70109/line-notify#contributing)

This is LINE Notify client SDK.

# Getting Started

## Get access token

```python
from line_notify.client import Client

client = Client(client_id='YOUR_CLIENT_ID', client_secret='YOUR_CLIENT_SECRET',
                redirect_uri='YOUR_URI')

access_token = client.get_access_token(code='NOTIFY_RESPONSE_CODE')
print(access_token)
# N6g50DiQZk5Xh...25FoFzrs2npkU3z
```

## Send Message
![push notify](https://i.imgur.com/RhvwZVm.png)

```python
from line_notify.client import Client

client = Client()
client.send(access_token='YOUR_ACCESS_TOKEN', params={
    'message': 'This is notify message'
})
# {'status': 200, 'message': 'ok'}
```

If your message is empty you will got:
```text
ValueError: {'status': 400, 'message': 'message: must not be empty'}
```

## Get Status
```python
from line_notify.client import Client

client = Client()
status = client.status(access_token='YOUR_ACCESS_TOKEN')
print(status)
# {'status': 200, 'message': 'ok', 'targetType': 'USER', 'target': 'NiJia Lin'}
```

## Revoke access token
![revoke token](https://i.imgur.com/7GAAzOi.png)

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