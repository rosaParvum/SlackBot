from slackclient import SlackClient
import sys

class Bot:

    def __init__(self, token):
        self.token = token
        print("Bot instantiated. My token is: "+self.token+".")

    def connect(self):
        print("Connecting with token: "+self.token+"...")

        self.client = SlackClient(self.token)
        self.client.rtm_connect()
        is_ok = self.client.api_call("api.test")
        is_ok = is_ok["ok"]

        if is_ok == True:  
            print("Connection established!")

        else:
            print("Error code : 1. Connection failure. Check access token?")
            sys.exit()
            
    def print_chat(self, msg, channel):
        self.client.rtm_send_message(channel, msg)

    def read_msg(self):
        msg = self.client.rtm_read()
        if len(msg) > 0:
            msg = msg[0]
            if "type" in msg:
                if msg["type"] == "message":
                    return msg

            return []
        else:
            return []
        
    def hello(self):
        self.client.api_call("chat.postMessage", token=self.token, channel="#general", text="Hello World", as_user=True)

    def id2name(self, id):
        users = self.client.api_call("users.list", token=self.token)
        users = users["members"]
        for user in users:
            if user["id"] == id:
                username = user["name"]
                return "@"+username
