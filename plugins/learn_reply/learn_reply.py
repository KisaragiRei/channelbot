from qqbot_handler import plugins
import qqbot
import csv
from config import admins
from message import reply

@plugins.register(qqbot.HandlerType.MESSAGE_EVENT_HANDLER, 'learn_reply')
async def learn_reply(event, message: qqbot.Message):
    if message.content.strip().startswith('/learn '):
        if message.author.id not in admins:
            reply('使用该命令的权限不足')
            return True
        with open('replies.txt') as f:
            reader = list(csv.reader(f))
            writer = csv.writer(open('replies.txt', 'w'))
            for i in reader:
                if message.content.split(' ')[1].strip() == i[0].strip():
                    i.append(message.content.split(' ')[2])
                    writer.writerows(reader)
                    await reply(message, '已添加')
                    return True
            reader.append([message.content.split(' ')[1].strip(), message.content.split(' ')[2].strip()])
            print(reader)
            writer.writerows(reader)
            await reply(message, '已学习')
            return True
    return False
    