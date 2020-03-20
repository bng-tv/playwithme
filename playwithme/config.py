from os import getenv
from uuid import uuid4

DEBUG: bool = getenv("DEBUG", "true").lower() == 'true'
SQLA_URI: str = getenv("SQLA_URI", "sqlite:///test.db")

IRC_NICK: str = getenv("IRC_NICK")
IRC_PASS: str = getenv("IRC_PASS")
IRC_CHAN: str = getenv("IRC_CHAN")
IRC_HOST: str = getenv("IRC_HOST", "irc.chat.twitch.tv")
IRC_PORT: int = int(getenv("IRC_PORT", "6697"))
IRC_TLS: bool = getenv("IRC_TLS", 'true').lower() == "true"
IRC_CMD: str = getenv("IRC_CMD", "^\!playwithme (?P<name>\w+ )?(?P<game>\w+)$")
IRC_HELP: str = getenv("IRC_HELP",
                       "To use this command, do !playwithme <in-game name> <game name, if missing it will be \"any\">")

WEB_TITLE: str = getenv("WEB_TITLE", "Play With Me")
WEB_HOST: str = getenv("WEB_HOST", "0.0.0.0")
WEB_PORT: int = int(getenv("WEB_PORT", "8080"))
WEB_SECRET: str = getenv("WEB_SECRET", str(uuid4()))
WEB_ADMIN: bool = getenv("ADMIN", "false").lower() == "true"
