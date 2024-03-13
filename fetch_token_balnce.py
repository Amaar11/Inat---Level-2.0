from web3 import Web3, HTTPProvider
from web3.exceptions import ABIFunctionNotFound
from abi import get_token_abi, addresses, tokens

# Povezivanje sa Ethereum blockchain
w3 = Web3(HTTPProvider("https://rpc.eth.gateway.fm"))

def balance(address, token_address, token_name):
    try:
        # Dohvati ABI podatke 
        token_abi = get_token_abi(token_address)
        if token_abi is None:
            raise Exception("ABI data not found for token")

        token_contract = w3.eth.contract(address=token_address, abi=token_abi)

        # Dohvati balans tokena za trenutni račun
        token_balance = token_contract.functions.balanceOf(address).call()
        return token_balance
    except ABIFunctionNotFound:
        print(f"ERROR: Function 'balanceOf' not found for token {token_name}")

# Testiranje funkcije balance
for address_type, address in addresses:
    print(f"Balans tokena za {address_type}: {address}")
    for token_name, token_address in tokens.items():
        token_balance = balance(address, token_address, token_name)
        if token_balance is not None:
            print(f"{token_name}: {token_balance}")
    print()
