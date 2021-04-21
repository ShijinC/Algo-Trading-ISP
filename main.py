from td_read import *
from td_get import *
from theory import *

rfr = 0.28
div = 0.0

aapl = load_option_chain("aapl")

option1 = aapl.calls[1]


test_price = Black_Scholes_Option_Price(
    option1.stockprice,
    option1.daystoexpiration/365,
    option1.strike,
    rfr,
    div,
    option1.TV/100
    )


print(option1.strike,option1.daystoexpiration)
print(option1.TOV)
print("\n\n\n\n")
print(option1.last)
print("\n")
print(test_price)
print("\n\n\n\n")
