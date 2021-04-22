import math
from td_get import *
from td_read import *
import autograd.numpy as np
from autograd.scipy.stats import norm
from autograd.extend import primitive, defvjp
from autograd import grad

#EVERYTHING IN PERCENTAGE VALUE
def Black_Scholes_Option_Price(spot=133.0,life=0.1,strike=130.0,volatility=0.5,rfr=0.02,dividend=0.0):
    #print(spot)
    #print(life)
    #print(strike)
    #print(volatility)
    #print(rfr)
    #print(dividend)
    d1 = (np.log(spot/strike) + life * (rfr - dividend + (volatility**2)/2)) / (volatility * (life**0.5))
    d2 = d1 - volatility * np.sqrt(life)
    price = spot * np.exp(dividend*-1*life) * norm.cdf(d1) - strike * np.exp(rfr*-1*life) * norm.cdf(d2)
    #print("d1:  " + str(d1))
    #print("d2:  " + str(d2))
    #print("Nd1:  " + str(norm.cdf(d1)))
    #print("Nd2:  " + str(norm.cdf(d2)))
    return price

""" def Black_Scholes_Option_Volatility(spot,strike,life,volatility,rfr,dividend):
    spot * math.exp(dividend*-1*life) * """

def vega(option,rfr,dividend):
    spot = option.stockprice
    life = option.daystoexpiration / 365
    strike = option.strike
    volatility = option.TV / 100
    d1 = math.log(spot/strike) + life * (rfr - dividend + (volatility**2)/2)
    d1 /= (volatility * math.sqrt(life))
    vega = spot * (math.exp(d1**2/-2) / math.sqrt(2*math.pi)) * math.sqrt(life)
    return vega

def vomma(option,rfr,dividend):
    spot = option.stockprice    
    life = option.daystoexpiration /365
    strike = option.strike
    volatility = option.TV / 100

    d1 = math.log(spot/strike) + life * (rfr - dividend + (volatility**2)/2)
    d1 /= (volatility * math.sqrt(life))
    d2 = d1 - volatility * math.sqrt(life)
    vomma = spot * math.exp(dividend*-1*life) * math.sqrt(life) * (1/math.sqrt(2*math.pi)) * math.exp(d1**2/-2) * (d1*d2/volatility)
    return vomma
#life and vol are pre_sized
def last(spot=133.0,life=0.1,strike=130.0,volatility=0.5,rfr=0.02,dividend=0.0):
    return Black_Scholes_Option_Price(spot,life, strike,volatility,rfr,dividend)

def dlast(spot=133.0,life=0.1,strike=130.0,volatility=0.5,rfr=0.02,dividend=0.0):
    dc = grad(Black_Scholes_Option_Price,2)
    return dc(spot,life,strike,volatility,rfr,dividend)

def ddlast(spot=133.0,life=0.1,strike=130.0,volatility=0.5,rfr=0.02,dividend=0.0):
    dc = grad(Black_Scholes_Option_Price,2)
    ddc = grad(dc,2)
    return ddc(spot,life,strike,volatility,rfr,dividend)

def double(x):
    return 2*x

def main():
    print("running main")
    
"""     ##checking vega
    rfr = 0.28
    div = 0.0

    aapl = load_option_chain("aapl")

    option1 = aapl.calls[1]

    theoretical_vega = vega(option1,rfr,div)
    print("theoretical vega = " + str(theoretical_vega) + " while real vega = " + str(option1.vega)) """

if __name__ == "__main__":
    main()


""" price2 = Black_Scholes_Option_Price(
    60,
    0.5,
    58,
    0.035,
    0.0125,
    0.20
)

print(price2)
 """