import requests
import numpy as np

r = requests.get("https://tradeogre.com/api/v1/orders/BTC-CCX")
json_object = r.json()

buyers = json_object['buy']
sellers = json_object['sell']

buyers_list = list(buyers.items())
best_buyer_ogre = buyers_list[-1]

sellers_list = list(sellers.items())
best_seller_ogre = sellers_list[0]

r = requests.get("https://api3.stex.com/public/orderbook/817")
json_object = r.json()

data = json_object['data']

best_buyer_stex = data['bid'][0]
best_seller_stex = data['ask'][0]

print('best_buyer_stex : ', best_buyer_stex,
      'best_seller_ogre : ', best_seller_ogre)

best_buyer_stex_price = float(best_buyer_stex['price'])
# best_buyer_stex_price = float(best_buyer_stex['price'])
best_seller_ogre_price = float(best_seller_ogre[0])
# best_seller_ogre_price = 0.00000901 // Test Debug


# best_buyer_ogre_price = float(best_buyer_ogre[0])


diff = best_buyer_stex_price - best_seller_ogre_price

if diff > 0:
    print('best_buyer_stex_price : ', best_buyer_stex_price)
    # print('best_buyer_ogre_price : ', best_buyer_ogre_price)

    print('amount best_buyer_stex', float(best_buyer_stex['amount']))
    print('amount best_buyer_ogre', float(best_buyer_ogre[1]))

    maximum_to_trade = min(
        float(best_buyer_stex['amount']), float(best_buyer_ogre[1]))
    print('maximum_to_trade : ', maximum_to_trade)

    price_to_buy = maximum_to_trade * best_seller_ogre_price
    print('price_to_buy : ', price_to_buy)

    price_to_sell = maximum_to_trade * best_buyer_stex_price
    print('price_to_sell : ', price_to_sell)

    price_to_buy_w_fee = maximum_to_trade * best_seller_ogre_price + \
        (maximum_to_trade * best_seller_ogre_price * 0.002)
    print('price_to_buy (w fees) : ', price_to_buy)

    price_to_sell_w_fee = maximum_to_trade * best_buyer_stex_price - \
        (maximum_to_trade * best_buyer_stex_price * 0.002)
    print('price_to_sell (w fees) : ', price_to_sell)
    if price_to_buy_w_fee < price_to_sell_w_fee:
        print('Jackpot !')
else:
    print('No gain !')


# async def g():
# print('AsyncG')

# import time

# while True:
#     time.sleep(1)
#     print("Hello !")
