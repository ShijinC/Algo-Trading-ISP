import tda

API_KEY = "c20020807"
REDIRECT_URL = "http://localhost:8080"
TOKEN_PATH = "token.json"

def make_webdriver():
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver

client = tda.auth.easy_client(
    API_KEY,
    REDIRECT_URL,
    TOKEN_PATH,
    make_webdriver)