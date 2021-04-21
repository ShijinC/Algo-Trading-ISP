import math
from scipy.stats import norm
from td_get import *
from td_read import *

#EVERYTHING IN PERCENTAGE VALUE
def Black_Scholes_Option_Price(option,rfr,dividend):
    spot = option.stockprice
    life = option.daystoexpiration / 365
    strike = option.strike
    volatility = option.TV / 100
    d1 = math.log(spot/strike) + life * (rfr - dividend + (volatility**2)/2)
    d1 /= (volatility * math.sqrt(life))
    d2 = d1 - volatility * math.sqrt(life)
    price = spot * math.exp(dividend*-1*life) * norm.cdf(d1)
    price -= strike * math.exp(rfr*-1*life) * norm.cdf(d2)
    print("d1:  " + str(d1))
    print("d2:  " + str(d2))
    print("Nd1:  " + str(norm.cdf(d1)))
    print("Nd2:  " + str(norm.cdf(d2)))
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


def RND(option,rfr,dividend):
    spot = option.stockprice
    life = option.daystoexpiration
    strike = option.strike
    volatility = option.TV / 100
    vega = option.vega
    vomma = vomma(option,rfr,dividend)
    d1 = math.log(spot/strike) + life * (rfr - dividend + (volatility**2)/2)
    d1 /= (volatility * math.sqrt(life))
    d2 = d1 - volatility * math.sqrt(life)
    probability = norm.cdf(d2) * (
        1/(volatility*strike*math.sqrt(life))+
        2*d1
    )

def main():
    

    ##checking vega
    rfr = 0.28
    div = 0.0

    aapl = load_option_chain("aapl")

    option1 = aapl.calls[1]

    theoretical_vega = vega(option1,rfr,div)
    print("theoretical vega = " + str(theoretical_vega) + " while real vega = " + str(option1.vega))

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