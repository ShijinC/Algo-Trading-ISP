import tda
import json

TD_API_KEY = "c20020807"
REDIRECT_URL = "http://localhost:8080"
TOKEN_PATH = "token.json"

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
                    self.calls.append(options(i))

class options():
    def __init__(self,dic):
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

#TD Ameritrade API Setup
def make_webdriver():
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver

client = tda.auth.easy_client(
    TD_API_KEY,
    REDIRECT_URL,
    TOKEN_PATH,
    make_webdriver)

#Calling fundamental data for aapl
r = client.get_option_chain(
    "AAPL",
    strike=131,
    #strike_count=5,
    include_quotes=True,
    strike_range=client.Options.StrikeRange.ALL,
    interval=1

    )

print(r)

#Writing data to file
with open('data.json', 'w') as outfile:
    json.dump(r.json(), outfile)
    
with open('data.json') as outfile:
    data = json.load(outfile)

aapl = option_chain(data)


print("\n",aapl.callraw)
print("\n\n\n\n\n")

print(aapl.calls[0])
print("\n")
print(aapl.calls[0].type)
print("\n")
print(aapl.calls[0].last)
print("\n")
print(aapl.calls[0].bid)
print("\n")