import click

from playwithme.bot import Bot
from playwithme.config import IRC_NICK, IRC_HOST, IRC_TLS, IRC_PORT, IRC_PASS, WEB_HOST, WEB_PORT, DEBUG
from playwithme.model import base
from playwithme.web import web as flask


@click.group()
def cli():
    pass


@cli.command()
def init():
    base.metadata.create_all()


@cli.command()
def bot():
    client = Bot(nickname=IRC_NICK, username=IRC_NICK, realname=IRC_NICK)
    client.run(IRC_HOST, tls=IRC_TLS, port=IRC_PORT, password=IRC_PASS)


@cli.command()
def web():
    flask.run(WEB_HOST, port=WEB_PORT, debug=DEBUG)


if __name__ == "__main__":
    cli()
