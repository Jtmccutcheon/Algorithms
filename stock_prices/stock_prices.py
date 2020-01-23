#!/usr/bin/python

import argparse


def find_max_profit(prices):
    # set up base case
    current_min = prices[0]
    max_profit = prices[1] - current_min

    for i in range(1, len(prices)):
        current_price = prices[i]
        if current_price - current_min > max_profit:
            max_profit = current_price - current_min
        if current_min > current_price:
            current_min = current_price

    return max_profit


if __name__ == '__main__':
        # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
