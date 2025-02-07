import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6997371758:AAENkbJIIq8eH2aFUuq67ttJWx3hqHcYe7Y")
    API_ID = int(os.environ.get("API_ID", "23407106"))
    API_HASH = os.environ.get("API_HASH", "34817fe096f567f55ce37750b8a5ff1b")
    #Add your channel id. For force Subscribe.
    CHANNEL = os.environ.get("CHANNEL", "")
    #Skip or add your proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = ''
