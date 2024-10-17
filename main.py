import api
import time
from pprint import pprint
import random

def getNum(fields, n):
    return fields[n]['value'].split("\nTotal - `")[1][:-1]

def getFromEmbed(message, n):
    return message[0]['embeds'][0].get(n)

def getCards(fields, n):
    cardList = []
    value = fields[n]['value']
    for i in value.split("[`")[1:]:
        cardList.append(i[2])
    return cardList

def convertCardsToNumbers(cards):
    #K, Q, J = 10  |  A = 1 or 11
    cardList = []
    d = {
        "A": 11,
        "K": 10,
        "Q": 10,
        "J": 10,
    }
    for card in cards:
        if d.get(card):
            cardList.append(d.get(card))
        else:
            cardList.append(int(card))
    return cardList

def sumOfList(l):
    sum = 0
    for i in l:
        sum += i
    return sum

def between(myNum, n1, n2):
    return myNum >= n1 and myNum <= n2

def hitOrStand(myNum, myCards, dankCard, isATrue):
    choice = "stand" #this removes all the else: choice = "stand" so we only need to check for hits
    
    sum = sumOfList(myCards)
    
    if sum <= 21 and isATrue: #soft hand
        if myNum < 18:
            choice = "hit"
        elif myNum == 18:
            if between(dankCard, 3, 6) or len(myCards) >= 3:
                choice = "hit"
        elif myNum >= 19:
            if len(myCards) >= 4:
                choice = "hit"
    
    else: #hard hand
        if myNum < 12:
            choice = "hit"
        
        elif between(myNum, 12, 16) and between(dankCard, 7, 11):
            choice = "hit"

        elif myNum == 12:
            if between(dankCard, 2, 3):
                choice = "hit"
            elif between(dankCard, 4, 6) and len(myCards) >= 3:
                choice = "hit"

        elif myNum == 13:
            if between(dankCard, 2, 3) and len(myCards) >= 3:
                choice = "hit"
            elif between(dankCard, 4, 6) and len(myCards) >= 4:
                choice = "hit"

        elif between(myNum, 14, 15) and between(dankCard, 2, 6) and len(myCards) >= 4:
            choice = "hit"

        elif myNum == 16:
            if between(dankCard, 2, 3) and len(myCards) >= 4:
                choice = "hit"

        elif myNum == 17:
            if between(dankCard, 2, 8):
                choice = "stand"
            if between(dankCard, 9, 11) and len(myCards) >= 4:
                choice = "hit"
    return choice

def playBlackJack(tokenObj):
    def play():
        time.sleep(1)
        message = tokenObj.getMessage(10)
        description = str(getFromEmbed(message, "description"))
        fields = getFromEmbed(message, "fields")
        myNum = int(getNum(fields, 0))
        myCards = getCards(fields, 0)
        isATrue = "A" in myCards
        myCards = convertCardsToNumbers(myCards)
        dankCard = convertCardsToNumbers(list(getCards(fields, 1)[0]))[0]
        if description[:10] == "**You lost" or description[:10] == "**You win!" or description[:10] == "**You tied":
            return 0
        else:
            print(myNum)
            print(myCards)
            print(dankCard)
            choice = hitOrStand(myNum, myCards, dankCard, isATrue)
            if choice == "hit":
                print(tokenObj.interactBlackJack("hit").text)
            elif choice == "stand":
                print(tokenObj.interactBlackJack("stand").text)
            play()

    while True:
        try:
            tokenObj.postMessage("pls bj max")
            play()
        except:
            print("Error Playing Black Jack..... Retrying in 10-15 seconds!")
        time.sleep(random.randint(10,12))

def playStream(tokenObj):
    strat = ["runAd", "readChat", "readChat", "readChat", "collectDonations"]
    while True:
        for strategy in strat[1:]:
            tokenObj.postMessage("pls stream")
            time.sleep(2)
            tokenObj.interactStream(strategy)
            tokenObj.postMessage(strategy)
            time.sleep(random.randint(60*10, 60*12))

def joinList(l):
    li = []
    if len(l) % 2 == 1:
        li.append(l[-1])
        l.pop(-1)
    for i in range(len(l)//2):
        li.append(l[i*2] + " " + l[i*2+1])
    return li


def tradeInventoryItems(tokenObj):
    tokenObj.postMessage("pls inv")
    data = []
    while True:
        items = tokenObj.interactInventory()
        if items != None:
            data.append(items)
        else:
            break
        time.sleep(1)
    print(data)
    data = joinList(data)
    print(data)
    for i in data:
        tokenObj.postMessage(f"pls trade {i}, 1 <@!user-id>")
        time.sleep(2)
        tokenObj.interactTrade()
        time.sleep(70)

def playScratch(tokenObj):
    while True:
        tokenObj.postMessage("pls scratch 1000")
        for i in range(3):
            time.sleep(1)
            tokenObj.interactScratch(i)
        time.sleep(2)

tokens = {
    "Mr. Stark": "token1",
    "Gary Oak": "token2"
}

stark = api.DiscordApi(tokens["Mr. Stark"], channel-id, guild-id)
# gary = api.DiscordApi(tokens["Gary Oak"], channel-id, guild-id)



playBlackJack(stark)
# playStream(stark)



# tradeInventoryItems(gary)
# tradeInventoryItems(stark)

# playScratch(stark)




# gary.postMessage("pls trade 2 life 1 poster 2 potato 63 purple 69 rabbit, 1 <@!user-id>")
# time.sleep(2)
# gary.interactTrade()