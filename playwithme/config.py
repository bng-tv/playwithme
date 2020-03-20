from os import getenv
from uuid import uuid4

DEBUG: bool = getenv("DEBUG", "true").lower() == 'true'
TITLE: str = getenv("TITLE", "Play With Me")

NICK: str = getenv("IRC_NICK")
PASS: str = getenv("IRC_PASS")
CHAN: str = getenv("IRC_CHAN")

HOST: str = getenv("IRC_HOST", "irc.chat.twitch.tv")
PORT: int = int(getenv("IRC_PORT", "6697"))
TLS: bool = getenv("IRC_TLS", 'true').lower() == "true"

COMMAND: str = getenv("COMMAND", "^\!playwithme (?P<name>\w+ )?(?P<game>\w+)$")
ADMIN: bool = getenv("ADMIN", "false").lower() == "true"

WEB_HOST: str = getenv("WEB_HOST", "0.0.0.0")
WEB_PORT: int = int(getenv("WEB_PORT", "8080"))
WEB_SECRET: str = getenv("WEB_SECRET", str(uuid4()))

SQLA_URI: str = getenv("SQLA_URI", "sqlite:///test.db")
