#!/usr/bin/env python

import click

from lotify.client import Client


@click.group()
def cli():
    pass


@cli.command()
@click.option('-t', '--access_token', type=str, help='LINE Notify access token', required=True)
@click.option('-m', '--message', type=str, help='send text message', required=True)
@click.option('-u', '--image-url', type=str, help='Send image with image url', default=None)
@click.option('-f', '--image-file', type=str, help='Send image file with local file', default=None)
def send_message(message, access_token, image_url, image_file):
    client = Client()
    if image_url is not None:
        client.send_message_with_image_url(access_token, message, image_url, image_url)
    elif image_file is not None:
        client.send_message_with_image_file(access_token, message, open(image_file, 'rb'))
    else:
        client.send_message(access_token, message)
    click.echo("Send notification success.")
