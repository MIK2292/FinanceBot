from myfinance import *
from myLaTeX import *

if __name__ == "__main__":
	bot = StockTradingBot(symbol="AAPL", short_window=15, long_window=60, initial_cash=10000)
	data, history = bot.run()
	
	pdf = LaTeX("Report")
	pdf.fill(history)
	pdf.compile()
