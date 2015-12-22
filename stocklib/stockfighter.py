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
        "price":int(price)*100,
        "direction":"buy",
        "orderType":"limit"
    }

    headers={
        "X-Starfighter-Authorization" : apikey
    }
    resp = requests.post("https://api.stockfighter.io/ob/api/venues/{0}/stocks/{1}/orders".format(venue,symbol),data=json.dumps(order),headers=headers)
    print resp.text
    return json.loads(resp.text)

def makeSellLimitOrder(account,symbol,venue,qty,price):

    order={
        "account":account,
        "qty":qty,
        "venue":venue,
        "symbol":symbol,
        "price":int(price)*100,
        "direction":"sell",
        "orderType":"limit"
    }

    headers={
        "X-Starfighter-Authorization" : apikey
    }
    resp = requests.post("https://api.stockfighter.io/ob/api/venues/{0}/stocks/{1}/orders".format(venue,symbol),data=json.dumps(order),headers=headers)
    print resp.text
    return json.loads(resp.text)

def getOrderStatus(orderid,symbol,venue):

    headers={
        "X-Starfighter-Authorization" : apikey
    }

    url="https://api.stockfighter.io/ob/api/venues/{0}/stocks/{1}/orders/{2}".format(venue,symbol,orderid)

    resp = requests.post(url,headers=headers)

    return json.loads(resp.text)

def cancelOrder(orderid,symbol,venue):

    headers={
        "X-Starfighter-Authorization" : apikey
    }

    url="https://api.stockfighter.io/ob/api/venues/{0}/stocks/{1}/orders/{2}".format(venue,symbol,orderid)

    resp = requests.post(url,headers=headers)

    return json.loads(resp.text)

def getStockInfo(symbol,venue):

    url="https://api.stockfighter.io/ob/api/venues/{0}/stocks/{1}/quote".format(venue,symbol)

    resp = requests.get(url)
    return json.loads(resp.text)
