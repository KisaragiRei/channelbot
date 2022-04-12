import qqbot
from config import token, enabled_plugins
from qqbot_handler import plugins

if __name__ == '__main__':
    [__import__(i) for i in enabled_plugins]
    qqbot.async_listen_events(token, False, *plugins)
