import tda
import json
import datetime

TD_API_KEY = "c20020807"
REDIRECT_URL = "http://localhost:8080"
TOKEN_PATH = "token.json"

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

def download_fundamentals(tickers):
    r = client.search_instruments(
        tickers,
        client.Instrument.Projection.FUNDAMENTAL
    )
    with open("./data/fundamentals.json", 'w') as outfile:
        json.dump(r.json(), outfile)
    print("Fundamental Data download complete")

def download_option_chain(ticker):
    r = client.get_option_chain(
        ticker,
        strike=134,
        strike_count=15,
        include_quotes=True,
        interval=2,
        from_date=datetime.datetime(2021, 5, 4),
        to_date=datetime.datetime(2021, 5, 6)
        )
    with open("./data/"+ticker+'.json', 'w') as outfile:
        json.dump(r.json(), outfile)

    print("\n","Option Chain Data Download Complete.")

def download_stock_quote(ticker):
    r = client.get_price_history(
        ticker,
        period_type=client.PriceHistory.PeriodType.YEAR,
        period=client.PriceHistory.Period.ONE_YEAR,
        frequency_type=client.PriceHistory.FrequencyType.WEEKLY,
        frequency=client.PriceHistory.Frequency.WEEKLY
        )
    with open("./data/s_"+ticker+'.json', 'w') as outfile:
        json.dump(r.json(), outfile)

    print("\n","Price History Data Download Complete.")

def main():
    
    init()
    #test_client()
    download_option_chain("SPY")
    #download_fundamentals("AAPL")
    #download_stock_quote("AAPL")

if __name__ == "__main__":
    main()