#!/usr/bin/env python

import click

from lotify.client import Client


@click.group()
def cli():
    pass


@cli.command()
@click.option('-t', '--access_token', type=str, help='LINE Notify access token', required=True)
@click.option('-m', '--message', type=str, help='send text message')
@click.option('-u', '--image-url', type=str, help='Send image with image url', default=None)
@click.option('-f', '--image-file', type=str, help='Send image file with local file', default=None)
@click.option('--sticker-package-id', type=str, help='Sticker package id', default=None)
@click.option('--sticker-id', type=str, help='Sticker id', default=None)
@click.option('-c', '--check-status', is_flag=True, help='Check status', default=False)
def send_message(message, access_token, image_url, image_file,
                 sticker_package_id, sticker_id, check_status):
    client = Client()
    if check_status:
        status = client.status(access_token)
        click.echo("Status: {status}".format(status=status))
    if image_url is not None:
        client.send_message_with_image_url(access_token, message, image_url, image_url)
    elif image_file is not None:
        client.send_message_with_image_file(access_token, message, open(image_file, 'rb'))
    elif sticker_package_id is not None and sticker_id is not None:
        client.send_message_with_sticker(access_token, message, sticker_id, sticker_package_id)
    else:
        client.send_message(access_token, message)
    click.echo("Send notification success.")
