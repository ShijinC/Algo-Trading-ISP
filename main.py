from td_read import *
from td_get import *
from theory import *

rfr = 0.02
div = 0

aapl = load_option_chain("aapl")

option1 = aapl.calls[0]


test_price = Black_Scholes_Option_Price(
    option1.stockprice,
    option1.daystoexpiration,
    option1.strike,
    rfr,
    div,
    option1.TV
    )

print(option1.TOV)
print("\n\n\n\n")
print(test_price)