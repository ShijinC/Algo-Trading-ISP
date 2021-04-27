import tda
import json
from download import *
from theory import *
#import pandas
#import numpy
import matplotlib.pyplot as plt
import csv


def load_sp500_list():
    sp500 = {}
    with open('data/s&p 500.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            sp500[row["Symbol"]] = []
            sp500[row["Symbol"]].append(row['Name'])
            sp500[row["Symbol"]].append(row['Sector'])
    return sp500
    

def load_trend(name):
    file = {}
    with open('data/'+name+'_trend.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            date = datetime.datetime.strptime(row["Day"], '%m/%d/%Y')
            file[date] = []
            file[date].append(float(row['doge: (United States)']))
    return file

def load_price(name):
    file = {}
    with open('data/'+name+'_price.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            date = datetime.datetime.strptime(row["Date"], '%m/%d/%Y')
            file[date] = []
            file[date].append(float(row['Closing Price (USD)']))
    return file

class stock():
    def __init__(self,option_chain,fundamental):
        self.option_chain = option_chain
        self.fundamental = fundamental

class option_chain():
    def __init__(self,data):
        assert data["status"]=="SUCCESS"
        self.symbol = data["symbol"]
        self.underlying = data["underlying"]
        self.callraw = data["callExpDateMap"]
        self.putraw = data["putExpDateMap"]
        self.calls = []
        self.puts = []
        for key,value in self.callraw.items():
            for k,v in value.items():
                for i in v:
                    self.calls.append(options(i,data["underlying"]["last"]))

class options():
    def __init__(self,dic,price):
        self.stockprice = float(price)
        self.type = dic["putCall"]
        self.bid = float(dic["bid"])
        self.ask = float(dic["ask"])
        self.strike = float(dic["strikePrice"])
        self.last = float(dic["last"])
        self.mark = float(dic["mark"])
        self.bidsize = float(dic["bidSize"])
        self.asksize = float(dic["askSize"])
        self.highprice = float(dic["highPrice"])
        self.lowprice = float(dic["lowPrice"])
        self.totalvol = float(dic["totalVolume"])
        self.volatility = float(dic["volatility"])
        self.delta = float(dic["delta"])
        self.gamma = float(dic["gamma"])
        self.theta = float(dic["theta"])
        self.vega = float(dic["vega"])
        self.rho = float(dic["rho"])
        self.openinterst = float(dic["openInterest"])
        self.timevalue = float(dic["timeValue"])
        self.TOV = float(dic["theoreticalOptionValue"])
        self.TV = float(dic["theoreticalVolatility"])
        self.expiredate = dic["expirationDate"]
        self.daystoexpiration = int(dic["daysToExpiration"])
        self.inthemoney = dic["inTheMoney"]
        self.intrinsic = self.stockprice - self.strike
        self.extrinsic = self.last - self.intrinsic


def load_option_chain(name):
    with open("./data/"+name+'.json') as outfile:
        data = json.load(outfile)
        data = option_chain(data)
        print("Option Chain Loaded")
        return data

def load_fundamental(name):
    with open("./data/fundamentals.json") as outfile:
        data = json.load(outfile)
        print("Fundamental Loaded")
        return data   

def define_graphing_metrics(options,trend=None,price=None):
    graphing_data = {}
    graphing_data["strike"] = [i.strike for i in options]
    graphing_data["extrinsic"] = [i.extrinsic for i in options]
    graphing_data["intrinsic"] = [i.intrinsic for i in options]
    graphing_data["price"] = [i.last for i in options]
    rfr = 0.03
    div = 0
    bins = 52
    high_strike = options[-1].strike
    low_strike = options[0].strike
    diff = high_strike - low_strike
    graphing_data["smooth_strike"] = [low_strike + 0.1*float(i) for i in range(int(diff)*10)]
    graphing_data["last"] = []
    graphing_data["dlast"] = []
    graphing_data["ddlast"] = []
    graphing_data["smooth_vol"] = []
    option = options[0]
    vol = volatility(options)
    for i in graphing_data["smooth_strike"]:
        graphing_data["smooth_vol"].append(vol(i))
        graphing_data["last"].append(last(option.stockprice,option.daystoexpiration/365,i,vol(i)/100,rfr,div))
        graphing_data["dlast"].append(dlast(option.stockprice,option.daystoexpiration/365,i,vol(i)/100,rfr,div))
        graphing_data["ddlast"].append(ddlast(option.stockprice,option.daystoexpiration/365,i,vol(i)/100,rfr,div))
        #graphing_data["last"].append(last(option.stockprice,option.daystoexpiration/365,i,option.TV/100,rfr,div))
        #graphing_data["dlast"].append(dlast(option.stockprice,option.daystoexpiration/365,i,option.TV/100,rfr,div))
        #graphing_data["ddlast"].append(ddlast(option.stockprice,option.daystoexpiration/365,i,option.TV/100,rfr,div))       

    graphing_data["totalvolume"] = sum([i.totalvol for i in options])
    graphing_data["relative_volume"] = [i.totalvol / graphing_data["totalvolume"] for i in options]
    graphing_data["totalopeninterest"] = sum([i.openinterst for i in options])
    graphing_data["relative_interest"] = [i.openinterst / graphing_data["totalopeninterest"] for i in options]
    graphing_data["interest"] = [i.openinterst for i in options]
    graphing_data["IV"] = [i.volatility for i in options]
    graphing_data["spread"] = [i.ask - i.bid for i in options]
    graphing_data["spread_ratio"] = [(i.ask - i.bid) / i.last for i in options]
    graphing_data["size_spread"] = [i.asksize - i.bidsize for i in options]
    graphing_data["underlying_price"] = options[0].stockprice
    if trend != None:
        graphing_data['trend_date'] = [key for key in trend]
        graphing_data['trend_score'] = [trend[key] for key in trend]
    if price != None:
        graphing_data['price_date'] = [key for key in price]
        graphing_data['price_price'] = [price[key] for key in price]
    return graphing_data


def make_graphs(data):
    gridspec = {
        'hspace':0.27,
        'wspace':0.27,
        'left':0.08,
        'right':0.96,
        'top':0.95,
        'bottom':0.05
    }

    fig, axs = plt.subplots(
        2,2,
        dpi=150,
        figsize=(6,6),
        gridspec_kw=gridspec
    )

    ############### RND ###############
    """ axs[0][0].plot(data["smooth_strike"],data["last"],color="C1",linewidth=1.0)
    #axs[0][0].scatter(data["strike"],data["last"],color="C1",marker='.')
    axs[0][0].grid()
    axs[0][0].set_title("Price vs Strike")
    axs[0][0].axvline(data["underlying_price"])

    axs[0][1].plot(data["smooth_strike"],data["dlast"],color="C0",linewidth=1.0)
    #axs[0][1].scatter(data["strike"][:-1],data["dlast"],color="C0",marker='.')
    axs[0][1].grid()
    axs[0][1].axvline(data["underlying_price"])
    axs[0][1].set_title("D_Price vs Strike")

    axs[1][0].plot(data["smooth_strike"],data["ddlast"],color="C2",linewidth=1.0)
    #axs[1][0].scatter(data["strike"][:-2],data["ddlast"],marker='.')
    axs[1][0].grid()
    axs[1][0].set_title("D_D_Price (Risk Neutral Distribution) vs Strike")
    axs[1][0].axvline(data["underlying_price"]) """
    ############### RND ###############

    ############### Trend ###############
    axs[0][0].plot(data["trend_date"],data["trend_score"],color="C1",linewidth=1.0)
    axs[0][0].twinx().plot(data["price_date"],data["price_price"],color="C3",linewidth=1.0)
    #axs[0][0].scatter(data["strike"],data["last"],color="C1",marker='.')
    axs[0][0].grid()
    axs[0][0].set_title("doge relatie interest vs doge exchange rate")
    ############### TREND ###############

    """ axs[0][1].plot(data["smooth_strike"],data["dlast"],color="C0")
    #axs[0][1].scatter(data["strike"][:-1],data["dlast"],color="C0",marker='.')
    axs[0][1].grid()
    axs[0][1].axvline(data["underlying_price"])
    axs[0][1].set_title("D_Price vs Strike")

    axs[1][0].plot(data["smooth_strike"],data["ddlast"],color="C2")
    #axs[1][0].scatter(data["strike"][:-2],data["ddlast"],marker='.')
    axs[1][0].grid()
    axs[1][0].set_title("D_D_Price (Risk Neutral Distribution) vs Strike")
    axs[1][0].axvline(data["underlying_price"])
    """
    
    axs[1][1].plot(data["strike"],data["IV"],color="C3")
    axs[1][1].twinx().plot(data["smooth_strike"],data["smooth_vol"],color="C3")
    axs[1][1].grid()
    axs[1][1].set_title("Implied Volatility vs Strike")
    axs[1][1].axvline(data["underlying_price"])
    
    plt.show()

def main():

    #fund = load_fundamental(["AAPL"])
    #aapl = stock(load_option_chain("aapl"),fund["AAPL"]["fundamental"])
    #print(aapl)

    file = load_trend("doge")
    print(file)

if __name__ == "__main__":
    main()