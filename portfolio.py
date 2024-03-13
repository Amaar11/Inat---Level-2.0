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

# Ovdje bi definirali vaše adrese i tokene
#addresses = [
#    ("Contract", "0x14052a178026665BB27fd0Be549f8FB8a88780d4"),
#    ("EOA", "0xC6A8109D566D31758329452c626D473B7815380E"),
#    ("EOA", "0xba42C2DfbB5e876EfD9dBd198DeD5DEB2beD68C5")
#]
#
#tokens = {
#    "USDC": "0x43506849D7C04F9138D1A2050bbF3A0c054402dd",
#    "GNO": "0x6810e776880C02933D47DB1b9fc05908e5386b96",
#    "GEL": "0x15b7c0c907e4C6b9AdaAaabC300C08991D6CEA05",
#    "COW": "0xDEf1CA1fb7FBcDC777520aa7f396b4E015F497aB",
#    "SWISE": "0xA28C2d79f0c5B78CeC699DAB0303008179815396",
#    "WBTC": "0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599"
#}

# Dohvat cijena tokena
token_ids = ["gnosis","gelato", "cow-protocol","usd-coin","stakewise","wrapped-btc-wormhole"]
token_prices = get_token_prices(token_ids)

# Izračun ukupne vrijednosti portfelja
total_values = calculate_total_portfolio_value(addresses, tokens, token_prices)

# Ispis rezultata
for address_type, value in total_values.items():
    print(f"Address Type: {address_type}, Total Portfolio Value: {value} USD")
