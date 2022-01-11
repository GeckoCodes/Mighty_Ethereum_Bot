""" Script to take the common tokens between the different dExchanges and 
    see if there are any price discrepancies
"""

# Run the imports
import json
import requests
from kyber_plugins import kyber_path
from python_1inch import OneInchExchange


def main():
    # First need to read in the list of common pairs
    with open("price_monitoring/common_tokens.json", "r") as json_file:
        _ = json.load(json_file)
    tokens = _['common_tokens']

    # Loop through the tokens and build up prices
    for token in tokens:

        print("="*50)
        print(f"Grabbing quotes for token: {token}")


        # Now have a list of common_tokens - need to get the price of each on the exchanges
        # Add any ethererum address
        eth_exchange = OneInchExchange('0xA8eF29f7B7dA9163D529B1080701212122752c74')
        test_response = eth_exchange.get_tokens() # works 
        
        # 1. 1Inch
        # Try getting an exchange quote
        exchange_response = eth_exchange.get_quote(from_token_symbol='ETH', to_token_symbol=token, amount=1)
        
        _1_inch_price = int(exchange_response['toTokenAmount']) / 10  ** exchange_response['toToken']['decimals']

        print(f"1Inch Price: 1 ETH == {_1_inch_price}")


        # 2. Kyber
        # Try getting an exchange quote
        exchange_response = eth_exchange.get_quote(from_token_symbol='ETH', to_token_symbol=token, amount=1)
        
        _1_inch_price = int(exchange_response['toTokenAmount']) / 10  ** exchange_response['toToken']['decimals']

        print(f"1Inch Price: 1 ETH == {_1_inch_price}")




if __name__== "__main__":
    main()