import tda
import json

TD_API_KEY = "c20020807"
REDIRECT_URL = "http://localhost:8080"
TOKEN_PATH = "token.json"

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
r = client.search_instruments("AAPL",client.Instrument.Projection.FUNDAMENTAL)

#Writing data to file
with open('data.txt', 'w') as outfile:
    json.dump(r.json(), outfile)

#Getting data from fred api
