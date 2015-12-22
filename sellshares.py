__author__ = 'Dzhambulat'

from stocklib.stockfighter import *
import math
import time

setApiKey('')

share_num=100000
current_num=0

account=''

symbol=''
venue=''
price_avg=0.0
prices=[]
info_num=30

for i in range(info_num):
    r=getStockInfo(symbol,venue)
    price_avg+=r['last']
    prices.append(r['last'])
    print (r['last'])
    time.sleep(3)
price_avg /= info_num

sqr_differs=[(p-price_avg)*(p-price_avg) for p in prices]
std=sum(sqr_differs)/25.0
std=math.sqrt(std)

print "Average price is "+ str(price_avg)
print "Std is "+str(std)

if(std>0):
    bid_price=price_avg/100.0-1.96*std/100.0+0.2
    ask_price=price_avg/100.0+1.96*std/100.0-0.2
else:
    bid_price=price_avg-0.2
    ask_price=price_avg+0.2

print "Bid price: "+str(bid_price)
print "Ask price: "+str(ask_price)

makeBuyLimitOrder(account,symbol,venue,10,bid_price)

#makeSellLimitOrder(account,symbol,venue,10,ask_price)
