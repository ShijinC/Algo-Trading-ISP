# Algo-Trading-ISP

## Progress

- Figured out how to use the API from TD Ameritrade and FRED (Federal Reserve Economic Data)
- Able to freely import data

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
- Basically any economic data
- Including historical data

Social Sentiment
- Rate Limit: 25/Day 5/s
- Stock Sentiment Score
- Industry Sentiment Score

## Current Ideas
- Using Option Chain data to create probability distribution of the underlying.
- Some kind of sentimental analysis. (Stocktwits API,DIY Twitter (Tweepy), SocialSentiment.io (free), google sentiment analysis tool)
- focus on comparative advantage adjusted for S&P 500
- Use getMovers from TD API 

- Have to have some kind of visualization, using matplotlib
- Have to have backtesting platform 
- TD API rate limit: 120/min   7200/hr   172800/day
- Reddit Algo Trading Side Bar resources.

## Next Steps

1. Build Backtesting platform (data handling - numpy&pandas?)
2. Produce a bunch of visualization on testing ideas
