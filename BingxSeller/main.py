import time

from loguru import logger

from settings import SYMBOL
from request import sell_token_by_limit_order, get_balance


logger.add('log.log', rotation='12:00', level='INFO')


def find_token_from_balance_list(balance: list, token: str) -> float | None:
    for i in balance:
        if i['asset'] == token:
            return float(i['free'])
    return False


def calc_min_sell_volume(price: float, amount: float):
    return True if price * amount > 5 else False


def main():
    price_sell = float(input('price sell: '))
    while True:
        token = SYMBOL.split('-')[0]
        balance = get_balance()
        token_balance = find_token_from_balance_list(balance['balances'], token)
        if not token_balance:
            logger.error(f"token: {token} not found in balance")
            continue

        if calc_min_sell_volume(price_sell, token_balance):
            sell_token_by_limit_order(price_sell, token_balance)
            logger.info(f'sold {token_balance} {token} by {price_sell}, total: {token_balance*price_sell}')
            break

        time.sleep(1)


if __name__ == '__main__':
    main()
