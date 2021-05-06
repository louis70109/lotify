import click
from lotify.client import Client


@click.group()
def cli():
    pass


@cli.command()
@click.option('-t', '--access_token', type=str, help='access token', required=True)
@click.option('-m', '--message', type=str, help='message to send', required=True)
@click.option('-u', '--image-url', type=str, help='image url to send', default="")
@click.option('-f', '--image-file', type=str, help='image file path to send', default="")
def send_message(message, access_token, image_url, image_file):
    client = Client()
    if image_url != "":
        client.send_message_with_image_url(access_token, message, image_url, image_url)
    elif image_file != "":
        client.send_message_with_image_file(access_token, message, open(image_file, 'rb'))
    else:
        client.send_message(access_token, message)
    click.echo("send successfully")
