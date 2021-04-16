# Algo-Trading-ISP

## Progress

- Figured out how to use the API from [TD Ameritrade](https://developer.tdameritrade.com/) and [FRED (Federal Reserve Economic Data)](https://fred.stlouisfed.org/docs/api/fred/)
- Able to freely import data from TD Ameritrade API, FRED API, and Sentiment API (examples in td_test.py, fred_test.py, and stm_test.py)
- formatted option chain data from td
- Ready to visualize

## Next Steps

1. Read Resources on creating distribution
2. Create distribution generation model
3. Travarse through selected targets
4. Trade the ones with the largest margin of error
5. Build backtesting platform to calculate performance data on the model
6. Visualize!!

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
