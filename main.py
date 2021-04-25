from reader import *
from download import *
from theory import *
from autograd import grad
import autograd.numpy as np


aapl = load_option_chain("aapl").calls
spy = load_option_chain("SPY").calls
option = aapl[0]
doge_trend = load_trend("doge")
doge_price = load_price("doge")
data = define_graphing_metrics(spy,doge_trend,doge_price)
make_graphs(data)

#sp500 = [key for key in load_sp500_list()]
#print(sp500)

""" #print(x)
#print([i for i in x])
print(dc(option1.stockprice,1.0,1.0,1.0,1.0,1.0))
print("\n\n\n")
print(ddc(option1.stockprice,1.0,1.0,1.0,1.0,1.0))
print("\n\n\n")
#print(Black_Scholes_Option_Price([option1.stockprice,option1.daystoexpiration/365,option1.strike,option1.TV/100,rfr,div]))
print("\n\n\n")
print(option1.last) """



""" price2 = Black_Scholes_Option_Price(
    60,
    0.5,
    58,
    0.20,
    0.035,
    0.0125
)

print(price2) """