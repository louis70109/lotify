# Introduction 
redirect_uri
client_id
client_secret
# Getting Started

## Send Message
```python
from line_notify.client import Client

client = Client()
client.send(access_token='p82k...0Xr', params={
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
status = client.status(access_token='p82k...0Xr')
print(status)
# {'status': 200, 'message': 'ok', 'targetType': 'USER', 'target': 'NiJia Lin'}
```
# Build and Test
TODO: Describe and show how to build your code and run the tests. 

# Contribute
TODO: Explain how other users and developers can contribute to make your code better. 

If you want to learn more about creating good readme files then refer the following [guidelines](https://docs.microsoft.com/en-us/azure/devops/repos/git/create-a-readme?view=azure-devops). You can also seek inspiration from the below readme files:
- [ASP.NET Core](https://github.com/aspnet/Home)
- [Visual Studio Code](https://github.com/Microsoft/vscode)
- [Chakra Core](https://github.com/Microsoft/ChakraCore)