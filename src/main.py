from typing import Tuple, Union
from common import Action
from math import ceil, floor

total_time = 182  # number of days
buying_frequency = 1  # amount of days
starting_value = 6000  # GBP

per_cycle_amount = starting_value * buying_frequency / total_time

portfolio: object

# region Action
def trade(portfolio, stock, amount: float, action: Action) -> bool:
    if action == Action.HOLD:
        return False

    shares = floor(per_cycle_amount / stock.pps)
    amount_to_invest = shares * stock.pps

    if action == Action.BUY:
        portfolio.bucket[stock.ticker] -= amount_to_invest
        portfolio.shares[stock.ticker] += shares

    if action == Action.SELL:
        portfolio.bucket[stock.ticker] += amount_to_invest
        portfolio.shares[stock.ticker] -= shares

    return True


def all_in(portfolio, stock) -> bool:
    action = Action.BUY
    amount = portfolio.bucket[stock.ticker]


# endregion


# region Rules

# If the stock has gone down since the past cycle you put more money in
def RULE_normal_down(stock):
    current_stock_price = 0
    previous_stock_price = 0

    if previous_stock_price < current_stock_price:
        invest_in(portfolio=portfolio, stock=stock, amount=per_cycle_amount)


# If the stock has gone above the so-far average then you sell a cycle amount

# If the stock has gone up by more than 50% of the initial amount you sell everything

# If the stock has gone down by more than 50% of the initial amount then you invest everything

# endregion


class Bucket(object):
    initial_investment: float
    ticker: str


class Portfolio(object):
    shares: dict
    buckets: dict
    time: int

    def __init__(self):
        self.buckets = {}

    def add_bucket(self, ticker: str, starting_amount: float):
        self.buckets[ticker] = get_current_price(time, ticker)  

    def cash(self):
        return self.bucket.values()


class Strategy(object):
    active_time: Tuple(int, int)  # The time of day you make your trades

    rules: list

    def __init__(self, active_time):
        self.active_time = active_time

    def apply(self, stock) -> Action:
        "Apply the rule set to the stock and return an Action."
        actions = {}

        action, amount = self.apply_rules(stock)

