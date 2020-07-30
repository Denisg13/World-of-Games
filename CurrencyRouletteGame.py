from forex_python.converter import CurrencyRates
import random

def get_money_interval(difficulty):
    c = CurrencyRates()
    rate = c.get_rate('USD', 'ILS')
    usd = random.randint(1, 100)
    print("USD: {0}".format(usd))
    return ((usd - (5 - difficulty)) * rate, (usd + (5 - difficulty)) * rate)

def get_guess_from_user():
    return float(input("Please enter your guess: "))

def play(difficulty):
    interval = get_money_interval(difficulty)
    user_guess = get_guess_from_user()
    
    if interval[0] <= user_guess <= interval[1]:
        return True
    else:
        return False
