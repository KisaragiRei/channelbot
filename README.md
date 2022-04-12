## 运行

安装依赖 `pip install -r requirements.txt`

在 `config.py` 中填写 `app_id` 和 `token` ，以及管理员在频道内的id，然后运行 `main.py` 即可。

## 插件编写

参照现有插件以及腾讯的 `api` 文档，将对应的函数注册到指定事件上，即可实现响应事件，以最简单的心跳检测插件为例：

```python
from qqbot_handler import plugins
import qqbot
from message import reply

# 将ping函数注册到频道消息事件上，当频道内收到消息时，ping函数就会被触发
@plugins.register(qqbot.HandlerType.MESSAGE_EVENT_HANDLER, 'ping_pong')
async def ping(event, message: qqbot.Message):
    if message.content.strip() == 'ping':
        await reply(message, 'pong') # 响应ping消息
        return True # 代表自己已经处理这条消息，不再继续广播消息
    return False # 这条消息不归ping管，继续向下广播
```

编写完成后，将插件的路径添加到 `config.py` 中的 `enabled_plugins` 中，当程序启动时即自动加载插件。




