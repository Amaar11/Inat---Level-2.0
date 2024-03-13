from fetch_token_balnce import balance
from abi import addresses, tokens
from price_token import get_token_prices

def calculate_total_portfolio_value(addresses, tokens, token_prices):
    total_values = {}
    for address_type, address in addresses:
        total_value = 0
        print(f"Calculating total portfolio value for {address_type}: {address}")
        for token_name, token_address in tokens.items():
            token_balance = balance(address, token_address)
            if token_balance is not None and token_name in token_prices and token_prices[token_name] is not None:
                token_value = token_balance * token_prices[token_name]
                total_value += token_value
                print(f"{token_name}: {token_balance} * {token_prices[token_name]} = {token_value} USD")
        total_values[address] = total_value
        print(f"Total value for {address_type}: {total_value} USD\n")
    return total_values

# Dohvat cijena tokena
token_ids = ["gnosis","gelato", "cow-protocol","usd-coin","stakewise","wrapped-btc-wormhole"]
token_prices = get_token_prices(token_ids)

# Izračun ukupne vrijednosti portfelja
total_values = calculate_total_portfolio_value(addresses, tokens, token_prices)

# Ispis rezultata
for address_type, value in total_values.items():
    print(f"Address Type: {address_type}, Total Portfolio Value: {value} USD")
