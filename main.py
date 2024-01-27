import timeit
from find_min_coins import find_min_coins
from find_coins_greedy import find_coins_greedy


def main():
    amounts_to_test = [113, 5555, 13, 58, 118, 558, 1118, 11908]
    iterations = 1000

    coin_denominations = [50, 25, 10, 5, 2, 1]
    print("| АЛГОРИТМ | СУМА | ЧАС ВИКОНАННЯ | РЕЗУЛЬТАТ |")
    print("| --- | --- | --- | --- |")

    for amount in amounts_to_test:
        dynamic_time = timeit.timeit(
            lambda: find_min_coins(amount, coin_denominations), number=iterations)
        greedy_time = timeit.timeit(lambda: find_coins_greedy(
            amount, coin_denominations), number=iterations)

        print(
            f"| Динамічне програмування | {amount} | {dynamic_time} | {find_min_coins(amount, coin_denominations)} |")
        print(
            f"| Жадібний алгоритм | {amount} | {greedy_time} | {find_coins_greedy(amount, coin_denominations)} |")
        # print("| --- | --- | --- | --- |")


if __name__ == "__main__":
    main()
