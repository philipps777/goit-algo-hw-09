def find_min_coins(amount, coin_denominations):

    min_coins = {denomination: 0 for denomination in coin_denominations}
    coins_used = {i: [] for i in range(amount + 1)}

    min_coins[0] = 0

    for current_amount in range(1, amount + 1):
        min_coins[current_amount] = float('inf')

        for coin in [c for c in coin_denominations if c <= current_amount]:
            if 1 + min_coins[current_amount - coin] < min_coins[current_amount]:
                min_coins[current_amount] = 1 + \
                    min_coins[current_amount - coin]
                coins_used[current_amount] = coins_used[current_amount - coin] + [coin]

    return {coin: coins_used[amount].count(coin) for coin in coins_used[amount]}


# def find_min_coins(amount, coin_denominations):
#     memo = {}

#     def d_function(target):
#         if target in memo:
#             return memo[target]

#         if target == 0:
#             return {}

#         if target < 0:
#             return None

#         min_coin_count = float('inf')
#         min_coin_combination = None

#         for coin in coin_denominations:
#             rest_amount = target - coin
#             rest_combination = d_function(rest_amount)

#             if rest_combination is not None:
#                 current_coin_count = rest_combination.get(coin, 0) + 1
#                 if current_coin_count < min_coin_count:
#                     min_coin_count = current_coin_count
#                     min_coin_combination = dict(rest_combination)
#                     min_coin_combination[coin] = min_coin_combination.get(
#                         coin, 0) + 1


#         memo[target] = min_coin_combination
#         return min_coin_combination

#     return d_function(amount)
