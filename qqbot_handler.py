import qqbot
from config import token

class List(list):
    def __init__(self):
        super().__init__()
        self.message_handler_list = []
        self.at_message_handler_list = []
        self.handlers = {
            qqbot.HandlerType.MESSAGE_EVENT_HANDLER: self.message_handler_list,
            qqbot.HandlerType.AT_MESSAGE_EVENT_HANDLER: self.at_message_handler_list
        }
        self.plugin_list = []
    def __str__(self):
        return str(self.plugin_list)

    def register(self, type, comment: str):
        '''
        向频道消息事件注册插件。

        若插件返回值为True，该插件运行完成后，不会继续广播消息
        反之继续广播消息

        type: 会被该插件响应的事件类型
        comment: 该插件的名称，会在主程序启动时被log出来
        '''
        def loader(f):
            self.handlers[type].append(f)
            self.plugin_list.append((comment, type))
            qqbot.logger.info(f'[插件管理] 插件 {type}.[{comment}] 成功加载')
            return f
        return loader

    async def message_broadcaster(self, event, message: qqbot.Message):
        '''
        向已注册的插件广播频道内普通消息的事件
        '''
        for func in self.message_handler_list:
            if await func(event, message):
                return

    async def at_message_broadcaster(self, event, message: qqbot.Message):
        '''
        广播频道内@bot的事件
        '''
        for func in self.at_message_handler_list:
            if await func(event, message):
                return

    def plugin_load(self):
        '''
        将broadcaster注册到sdk的回调函数上
        '''
        self.append(qqbot.Handler(qqbot.HandlerType.MESSAGE_EVENT_HANDLER, self.message_broadcaster))
        self.append(qqbot.Handler(qqbot.HandlerType.AT_MESSAGE_EVENT_HANDLER, self.at_message_broadcaster))

plugins = List()
plugins.plugin_load()
