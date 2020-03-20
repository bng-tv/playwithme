import click

from playwithme.bot import Bot
from playwithme.config import NICK, HOST, TLS, PORT, PASS, WEB_HOST, WEB_PORT, DEBUG
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
    client = Bot(nickname=NICK, username=NICK, realname=NICK)
    client.run(HOST, tls=TLS, port=PORT, password=PASS)


@cli.command()
def web():
    flask.run(WEB_HOST, port=WEB_PORT, debug=DEBUG)


if __name__ == "__main__":
    cli()
