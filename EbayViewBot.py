import requests
from threading import Thread
from user_agent import generate_user_agent, generate_navigator
import threading
import time

def viewItem(itemID, viewNum, useragent):
    headers = {
        'User-Agent':useragent,
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
    }
    requests.get('https://www.ebay.com/itm/'+str(itemID), headers=headers)
    print("VIEW # " + str(viewNum) )

def go(numOfViews, itemID):
    for i in range(numOfViews):
        t = Thread(target = viewItem, args = (itemID, i, generate_user_agent()))
        t.start()
        time.sleep(.1)

viewNum = input('How many views do you want?')
itemID = input('What is your item ID?')
go(int(viewNum), itemID)
