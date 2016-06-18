from slackclient import SlackClient

class Bot:

    def __init__(self, token):
        self.sc = SlackClient(token)
        self.token = token

    def read_msg(self):
        if self.sc.rtm_connect():
            print("Connection Established")


    def hello(self):
        self.sc.api_call("chat.postMessage", channel="#general", text="Hello World")
    
