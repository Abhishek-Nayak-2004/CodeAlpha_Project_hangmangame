import requests
from datetime import datetime

class StockPortfolioTracker:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, ticker, quantity):
        if ticker in self.portfolio:
            self.portfolio[ticker]['quantity'] += quantity
        else:
            self.portfolio[ticker] = {
                'quantity': quantity,
                'price': None,
                'last_updated': None
            }
        print(f"Added {quantity} shares of {ticker} to the portfolio.")

    def remove_stock(self, ticker):
        if ticker in self.portfolio:
            del self.portfolio[ticker]
            print(f"Removed {ticker} from the portfolio.")
        else:
            print(f"Ticker {ticker} not found in the portfolio.")

    def update_prices(self):
        api_url = "https://api.example.com/stock"  # Replace with a real API endpoint
        api_key = "your_api_key_here"  # Replace with your actual API key

        for ticker in self.portfolio.keys():
            try:
                response = requests.get(f"{api_url}/{ticker}", params={"apikey": api_key})
                response.raise_for_status()
                data = response.json()

                self.portfolio[ticker]['price'] = data['latestPrice']  # Adjust according to API response
                self.portfolio[ticker]['last_updated'] = datetime.now()

                print(f"Updated {ticker}: {data['latestPrice']}")

            except requests.exceptions.RequestException as e:
                print(f"Error updating {ticker}: {e}")

    def calculate_portfolio_value(self):
        total_value = 0
        for ticker, details in self.portfolio.items():
            if details['price'] is not None:
                total_value += details['quantity'] * details['price']
        return total_value

    def display_portfolio(self):
        print("\nYour Portfolio:")
        for ticker, details in self.portfolio.items():
            print(f"{ticker}: {details['quantity']} shares, \
                  Latest Price: {details['price']}, \
                  Last Updated: {details['last_updated']}")

if __name__ == "__main__":
    tracker = StockPortfolioTracker()

    # Example usage
    tracker.add_stock("AAPL", 10)
    tracker.add_stock("GOOGL", 5)
    tracker.add_stock("TATA", 25)
    tracker.add_stock("MRF", 10)
    tracker.update_prices()  
    tracker.display_portfolio()

    print(f"Total Portfolio Value: ${tracker.calculate_portfolio_value():.2f}")