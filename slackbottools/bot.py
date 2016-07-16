from slackclient import SlackClient

class Bot:

    def __init__(self, token):
        self.token = token
        print(self.token)

    def connect(self):
        print(self.token)
        self.client = SlackClient(self.token)
        self.client.rtm_connect(self.token)

    def print_chat(self, msg, channel):
        self.client.rtm_send_message(channel, msg)

    def read_msg(self):
           return(self.client.rtm_read())

    def hello(self):
        self.client.api_call("chat.postMessage", token=self.token, channel="#general", text="Hello World", as_user=True)
