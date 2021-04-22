from td_read import *
from td_get import *
from theory import *
from autograd import grad
import autograd.numpy as np

rfr = 0.002
div = 0.0

aapl = load_option_chain("aapl")

option1 = aapl.calls[0]
options = aapl.calls
data = define_graphing_metrics(options)
make_graphs(data)


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