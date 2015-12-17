__author__ = 'Dzhambulat'

import requests
import json

apikey=""

def setApiKey(key):
    global apikey
    apikey=key

def makeBuyLimitOrder(account,symbol, venue, qty, price):

    order={
        "account":account,
        "qty":qty,
        "venue":venue,
        "symbol":symbol,
        "price":price*100,
        "direction":"buy",
        "orderType":"limit"
    }

    headers={
        "X-Starfighter-Authorization" : apikey
    }
    req = requests.post("https://api.stockfighter.io/ob/api/venues/{0}/stocks/{1}/orders".format(venue,symbol),data=json.dumps(order),headers=headers)
    print req.text
