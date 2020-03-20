import pydle
import re
from playwithme.config import CHAN, COMMAND
from playwithme.model import StorageModel, session


class Bot(pydle.Client):
    async def on_connect(self):
        await super(Bot, self).on_connect()
        await self.join("#" + CHAN.lstrip("#"))

    async def on_message(self, target, by, message):
        await super(Bot, self).on_message(target, by, message)
        regex = re.compile(COMMAND)
        search = regex.search(message)
        search = search.groupdict() if search is not None else None
        if search is not None:
            if search['name'] is None:
                search['name'] = search['game']
                search['game'] = 'any'
            ses = session()
            ses.add(StorageModel(
                twitch=by,
                handle=search['name'],
                game=search['game']
            ))
            ses.commit()
