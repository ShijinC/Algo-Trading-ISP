import tda
import json
import datetime

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

#TD Ameritrade API Setup
def make_webdriver():
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver

def init():
    global client
    client = tda.auth.easy_client(
        TD_API_KEY,
        REDIRECT_URL,
        TOKEN_PATH,
        make_webdriver)

def test_client():
    print(client.get_quote("aapl").json())

def download_option_chain(ticker):
    r = client.get_option_chain(
        ticker,
        strike=134,
        strike_count=50,
        include_quotes=True,
        interval=2,
        from_date=datetime.datetime(2021, 4, 19),
        to_date=datetime.datetime(2021, 4, 25)
        )
    with open("./data/"+ticker+'.json', 'w') as outfile:
        json.dump(r.json(), outfile)

    print("\n","Data Download Complete.")

def main():
    
    init()
    test_client()
    download_option_chain("AAPL")

if __name__ == "__main__":
    main()