import requests

def get_token_prices(token_ids):
    api_url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": ",".join(token_ids),  # Spajamo sve token ID-ove u jedan string razdvojen zarezima
        "vs_currencies": "usd"       # Specifikujemo valutu u kojoj želimo dobiti cijene (USD)
    }
    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        data = response.json()
        prices = {}
        for token_id in token_ids:
            if token_id in data:
                prices[token_id] = data[token_id]["usd"]
            else:
                prices[token_id] = None  # Ako token ID nije pronađen, postavljamo cijenu na None
        return prices
    else:
        print("Error:", response.status_code)
        return None


token_ids = [ "gnosis","gelato", "cow-protocol","usd-coin","stakewise","wrapped-btc-wormhole"]

# Pozivamo funkciju i dobijamo trenutne cijene za sve tokene
token_prices = get_token_prices(token_ids)
print("Trenutne cijene:")
for token_id, price in token_prices.items():
    print(f"{token_id}: {price} USD " if price is not None else f"{token_id}: N/A")
