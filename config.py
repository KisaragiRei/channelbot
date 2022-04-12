from qqbot import Token
app_id = 'appid_here'
access_token = 'token_here'
token = Token(app_id, access_token)
enabled_plugins = [
    'plugins.helloworld.helloworld',
    'plugins.ping_pong.ping_pong',
    'plugins.learn_reply.learn_reply',
    'plugins.reply_learnt.reply_learnt',
]
admins = ['id of admins here']
