
import yfinance as yf

class StockTradingBot:
	def __init__(self, symbol, short_window, long_window, initial_cash):
		self.symbol = symbol
		self.short_window = short_window
		self.long_window = long_window
		self.cash = initial_cash
		self.stock_balance = 0
		self.history = []

	def get_stock_data(self, start_date, end_date):
		data = yf.download(self.symbol, start=start_date, end=end_date)
		return data

	def calculate_sma(self, data, window):
		return data['Close'].rolling(window=window).mean()

	def buy(self, price, amount, date):
		total_cost = price * amount
		if self.cash >= total_cost:
			self.cash -= total_cost
			self.stock_balance += amount
			self.history.append(f"{date}: Bought {amount} shares at ${price:.2f} each")

	def sell(self, price, amount, date):
		if self.stock_balance >= amount:
			total_sale = price * amount
			self.cash += total_sale
			self.stock_balance -= amount
			self.history.append(f"{date}: Sold {amount} shares at ${price:.2f} each")

	def execute_strategy(self, data):
		short_sma = self.calculate_sma(data, self.short_window)
		long_sma = self.calculate_sma(data, self.long_window)
		for i in range(self.long_window, len(data)):
			if short_sma.iloc[i] > long_sma.iloc[i]:
				# Buy signal: Short-term SMA crosses above Long-term SMA
				self.buy(data['Close'].iloc[i], 10, data.index[i]) 
				# Example: Buy 10 shares
			elif short_sma.iloc[i]:
				# Sell signal: Short-term SMA crosses below Long-term SMA
				self.sell(data['Close'].iloc[i], 10, data.index[i]) 
				# Example: Sell 10 shares

	def run(self):
		data = self.get_stock_data("2022-01-01", "2023-01-01") # Adjust date range as needed
		#print(data)
		self.execute_strategy(data)
		self.display_portfolio(data)
		return data, self.history

	def display_portfolio(self, data):
		print(f"Portfolio Summary:")
		print(f"Cash: ${self.cash:.2f}")
		print(f"Stock Balance: {self.stock_balance} shares")
		print(f"Portfolio Value: ${(self.cash + self.stock_balance * data['Close'].iloc[-1]):.2f}")
		#print()
		#print(*self.history, sep="\n")

#if __name__ == "__main__":
#	bot = StockTradingBot(symbol="AAPL", short_window=15, long_window=60, initial_cash=10000)
#	bot.run()
	
	










