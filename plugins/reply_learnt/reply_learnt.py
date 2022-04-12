from qqbot_handler import plugins
import qqbot
from message import reply
import random
import csv

@plugins.register(qqbot.HandlerType.MESSAGE_EVENT_HANDLER, 'reply_learnt')
async def reply_learnt(event, message: qqbot.Message):
    with open('replies.txt') as f:
        li = list(csv.reader(f))
    for j in li:
        if j[0].strip() == message.content.strip():
            await reply(message, random.choice(j[1:]).strip())
            return True
    return False