import math
from scipy.stats import norm

def Black_Scholes_Option_Price(spot,life,strike,rfr,dividend,volatility):
    d1 = math.log(spot/strike) + (rfr - dividend - math.pow(volatility,2) * life) 
    d1 /= volatility * math.sqrt(life)
    d2 = d1 - volatility * math.sqrt(life)
    price = spot * math.exp(dividend*-1*life) * norm.cdf(d1)
    price -= strike * math.exp(rfr*-1*life) * norm.cdf(d2)
    return price

