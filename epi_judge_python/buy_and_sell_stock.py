from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    dp = [0 for i in range(len(prices))]
    for i in range(0, len(prices)):
        for j in range(0, i):
            profit = round(prices[i] - prices[j], 2)
            if dp[i] == 0:
                dp[i] = max(dp[i-1], profit)
            else:
                dp[i] = max(dp[i], profit)
    return dp[len(prices) - 1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
