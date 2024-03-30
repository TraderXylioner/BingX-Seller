from CryptoMathTrade.exchange.bingx import Spot
from CryptoMathTrade.exchange.bingx import Account
from CryptoMathTrade.types import OrderBook, Side

from settings import API, SYMBOL


def sell_token_by_limit_order(price: float, amount: float):
    Spot(API.KEY, API.SECRET).new_limit_order(SYMBOL, Side.SELL, price, amount)


def get_balance():
    return Account(API.KEY, API.SECRET).get_balance().data
