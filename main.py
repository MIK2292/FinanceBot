

from myfinance import *
from myPDF import *
from myLaTeX import *

if __name__ == "__main__":
	bot = StockTradingBot(symbol="AAPL", short_window=15, long_window=60, initial_cash=10000)
	bot.run()
