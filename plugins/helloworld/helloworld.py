from qqbot_handler import plugins
import qqbot
from config import token

@plugins.register(qqbot.HandlerType.AT_MESSAGE_EVENT_HANDLER, 'helloworld')
async def hellosekai(event, message: qqbot.Message):
    if message.content.strip() == f'<@!{qqbot.UserAPI(token, False).me().id}>':
        msg_api = qqbot.AsyncMessageAPI(token, False)
        ref = qqbot.model.message.MessageReference()
        ref.message_id = message.id
        send = qqbot.MessageSendRequest(
            content='我在，有什么事吗', 
            msg_id = message.id,
            message_reference = ref
        )
        await msg_api.post_message(message.channel_id, send)
        qqbot.logger.info(f'[回复消息] {send.content} -> {qqbot.ChannelAPI(token, False).get_channel(message.channel_id).name}.{message.author.username}."{message.content}"')
        return True
    return False