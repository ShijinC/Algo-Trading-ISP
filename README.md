# Algo-Trading-ISP

## Progress
- used autodiff to obtain RNDs
- implemented BS formula in python 
- Made rough visualizations using matplotlib
- formatted option chain data from td
- Able to freely import data from TD Ameritrade API, FRED API, and Sentiment API (examples in td_test.py, fred_test.py, and stm_test.py)
- Figured out how to use the API from [TD Ameritrade](https://developer.tdameritrade.com/) and [FRED (Federal Reserve Economic Data)](https://fred.stlouisfed.org/docs/api/fred/)

## Next Steps

1. Calculate volatility for RNDs
2. Scale code to general tickers
3. unload dataset - done by 23rd
4. get data from Google Trend API
5. Produce more visuals based on categories
6. Make rough algorithm - done by 24th
7. Make backtesting frame
8. produce performance stats - done by 25th
9. Make powerpoint - done by 26th

### Avaliable Data:

TD Ameritrade
- Instrument Info (fundamental & technical of stocks)
- Account Info
- Option Chain (option data of stocks)
- Price History (Historical data of stocks)
- Current Quote
- Transaction History
- Saved Order
- Get Mover ()

FRED API (Federal Reserve Economic Data)
- [Basically any economic data](https://fred.stlouisfed.org/)
- Including historical data

Social Sentiment
- Rate Limit: 25/Day 5/s
- Stock Sentiment Score
- Industry Sentiment Score

## Current Ideas
- Using Option Chain data to create probability distribution of the underlying.

## Resources
- [fredapi documentation](https://github.com/mortada/fredapi)
- [TD API doumentation](url)
- [Option Based Risk-Neutual Probability Distribution](https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr677.pdf)
- [Butterfly](https://www.morganstanley.com/content/dam/msdotcom/en/assets/pdfs/Options_Probabilities_Exhibit_Link.pdf)
- [Calculation Paper](https://www.bankofengland.co.uk/-/media/boe/files/ccbs/resources/deriving-option-implied-probability-densities-for-foreign-exchange-markets.pdf)
- [Google Trend](https://trends.google.com/trends/explore?geo=US&q=doge)
- [Google Trend API](https://towardsdatascience.com/google-trends-api-for-python-a84bc25db88f)
