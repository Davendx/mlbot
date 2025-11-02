from asyncio import sleep
from ..telegram_helper.message_utils import delete_message
from ... import bot_loop

class AutoDeleteMessage:
    def __init__(self, client, message):
        self.client = client
        self.message = message
        bot_loop.create_task(self.start_delete())

    async def start_delete(self):
        await sleep(10)
        try:
            await delete_message(self.message)
        except Exception:
            pass
