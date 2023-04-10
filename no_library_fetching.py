import requests
# api doc : https://www.coingecko.com/en/api/documentation

def fetch_crypto_data(ids:str):

    url = f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids={ids}&order=market_cap_desc&per_page=100&page=1&sparkline=false"
    # sends a request to the API and returns the JSON data as a Python object
    response = requests.get(url)
    return response.json()

def fetch_historical_prices(crypto_id, days, interval="daily"):
    url = f"https://api.coingecko.com/api/v3/coins/{crypto_id}/market_chart?vs_currency=usd&days={days}&interval={interval}"
    # sends a request to the API and returns the JSON data as a Python object
    response = requests.get(url)
    return response.json()


def main():
    crypto_ids = "bitcoin,ethereum,uniswap,lido-dao,chainlink"
    cryptos_data = fetch_crypto_data(crypto_ids)

    for crypto in cryptos_data:
        symbol = crypto['symbol'].upper()
        current_price = crypto['current_price']

        historical_prices = fetch_historical_prices(crypto['id'], days=30)
        # Check if the historical_prices contain any data
        if historical_prices['prices']:
            last_month_price = historical_prices['prices'][0][1]
            monthly_change = ((current_price - last_month_price)/last_month_price)*100
        else:
            print(f"Error fetching historical data for {symbol}. Skipping...")
            continue

        print(f"{symbol} Current Price: {current_price}, Monthly Change: {monthly_change}")

if __name__ == "__main__":
    main()
