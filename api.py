import requests
import json
from pprint import pprint
import random
import string

class DiscordApi:
    def __init__(self, token, channel, guild):
        self.token = token
        self.channel = channel
        self.guild = guild
        self.counter = 0
        self.headers = {
            "authorization": self.token,
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"
        }

    def postMessage(self, content):
        self.headers["content-type"] = "application/json"
        content = json.dumps({"content": content})
        return requests.post(f"https://discord.com/api/channels/{self.channel}/messages", headers=self.headers, data=content)

    def getMessage(self, limit=50):
        return requests.get(f"https://discord.com/api/channels/{self.channel}/messages?limit={limit}", headers=self.headers).json()
    
    def postButton(self, customId, messageId):
        self.headers["content-type"] = "application/json"
        data = json.dumps({
            "type": 3,
            "application_id": "270904126974590976", #dank memer discord id
            "message_id": messageId,
            "guild_id": self.guild,
            "channel_id": self.channel,
            "data": {
                "component_type": 2, #ig it has to do with the type of component
                "custom_id": customId
            },
            "session_id": ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        })
        print(data)
        return requests.post("https://discord.com/api/v9/interactions", headers=self.headers, data=data)
    
    def interactBlackJack(self, choice):
        messages = self.getMessage(10)
        for message in messages:
            if message.get("components"):
                buttons = message["components"][0]["components"]
                hit = buttons[0]["custom_id"]
                stand = buttons[1]["custom_id"]
                if choice == "hit":
                    return self.postButton(hit, message["id"])
                if choice == "stand":
                    return self.postButton(stand, message["id"])

    def interactStream(self, choice):
        messages = self.getMessage(10)
        for message in messages:
            if message.get("components"):
                buttons = message["components"][0]["components"]
                readAd = buttons[0]["custom_id"]
                readChat = buttons[1]["custom_id"]
                collectDonations = buttons[2]["custom_id"]
                if choice == "readAd":
                    return self.postButton(readAd, message["id"])
                if choice == "readChat":
                    return self.postButton(readChat, message["id"])
                if choice == "collectDonations":
                    return self.postButton(collectDonations, message["id"])
    
    def interactInventory(self):
        messages = self.getMessage(10)
        for message in messages:
            if message.get("components"):
                itemList = ""
                items = message["embeds"][0]["description"].split("\n\n")
                
                for i in items:
                    amount = i.split("\n*ID* ")[0].split("** ─ ")[1].replace(",","") #amount of item
                    id = i.split("\n*ID* ")[1].split("` ─")[0][1:] #id of item
                    itemList += f"{amount} {id} "
                
                itemList = itemList[:-1]

                nextButton = message["components"][-1]["components"][2]
                if not nextButton.get("disabled"):
                    nextButton = nextButton["custom_id"]
                    self.postButton(nextButton, message["id"])
                    self.counter = 0
                else:
                    self.counter += 1
                if self.counter <= 1:
                    return itemList
                else:
                    return None

    def interactTrade(self):
        messages = self.getMessage(10)
        for message in messages:
            if message.get("components"):
                trade = message["components"][0]["components"][1]["custom_id"]
                print(trade)
                return self.postButton(trade, message["id"])

    def interactScratch(self, num):
        messages = self.getMessage(10)
        for message in messages:
            if message.get("components"):
                scratch = message["components"][0]["components"][num]["custom_id"]
                pprint(scratch)
                return self.postButton(scratch, message["id"])