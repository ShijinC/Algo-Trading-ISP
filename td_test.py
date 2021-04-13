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
r = client.get_option_chain(
    "AAPL",
    strike=131,
    strike_count=5,
    include_quotes=True,
    strike_range=client.Options.StrikeRange.ALL,
    interval=5

    )

print(r)
print(r.status_code)

#Writing data to file
with open('data.txt', 'w') as outfile:
    json.dump(r.json(), outfile)

