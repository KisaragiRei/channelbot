import qqbot
from config import token

async def reply(message: qqbot.Message, text: str):
    msg_api = qqbot.AsyncMessageAPI(token, False)
    ref = qqbot.model.message.MessageReference()
    ref.message_id = message.id
    send = qqbot.MessageSendRequest(
        content=text,
        msg_id = message.id,
        message_reference = ref
    )
    await msg_api.post_message(message.channel_id, send)
    qqbot.logger.info(f'[回复消息] {send.content} -> {qqbot.ChannelAPI(token, False).get_channel(message.channel_id).name}.{message.author.username}."{message.content}"')
