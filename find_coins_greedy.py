
def find_coins_greedy(amount, coin_denominations):

    coin_count = {denomination: 0 for denomination in coin_denominations}

    for denomination in coin_denominations:
        coin_count[denomination] = amount // denomination
        amount %= denomination

    return coin_count
