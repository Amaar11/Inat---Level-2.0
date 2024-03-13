import requests
from web3 import Web3, HTTPProvider
from web3.exceptions import ABIFunctionNotFound


# Povezivanje sa Ethereum blockchain
w3 = Web3(HTTPProvider("https://rpc.eth.gateway.fm"))

# Adrese računa za koje želite dohvatiti balanse
addresses = [
    ("Contract", "0x14052a178026665BB27fd0Be549f8FB8a88780d4"),
    ("EOA", "0xC6A8109D566D31758329452c626D473B7815380E"),
    ("EOA", "0xba42C2DfbB5e876EfD9dBd198DeD5DEB2beD68C5")
]

# Adrese tokena
tokens = {
    "USDC": "0x43506849D7C04F9138D1A2050bbF3A0c054402dd",
    "GNO": "0x6810e776880C02933D47DB1b9fc05908e5386b96",
    "GEL": "0x15b7c0c907e4C6b9AdaAaabC300C08991D6CEA05",
    "COW": "0xDEf1CA1fb7FBcDC777520aa7f396b4E015F497aB",
    "SWISE": "0xA28C2d79f0c5B78CeC699DAB0303008179815396",
    "WBTC": "0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599"
}

# Funkcija za dohvaćanje ABI podataka s Etherscan API-ja
def get_token_abi(token_address):
    api_url = f"https://api.etherscan.io/api?module=contract&action=getabi&address={token_address}&apikey=G4Z71GSAI5U1GFU97P1JBYVDTFAQW68UJ2"
    response = requests.get(api_url)
    abi = response.json()['result']
    return abi

abi_data = {}
for token_name, token_address in tokens.items():
    abi = get_token_abi(token_address)
    abi_data[token_name] = abi

# Ispis ABI podataka
for token_name, abi in abi_data.items():
    print(f"ABI podaci za {token_name}:")
    print(abi)
    print("\n")
