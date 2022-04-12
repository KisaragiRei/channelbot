from qqbot_handler import plugins
import qqbot
from message import reply

@plugins.register(qqbot.HandlerType.MESSAGE_EVENT_HANDLER, 'ping_pong')
async def ping(event, message: qqbot.Message):
    if message.content.strip() == 'ping':
        await reply(message, 'pong')
        return True
    return False