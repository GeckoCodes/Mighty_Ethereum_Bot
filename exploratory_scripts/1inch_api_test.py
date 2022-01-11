""" Script to test the 1inch Python API
"""

# Import the package
from python_1inch import OneInchExchange
from pprint import pprint

# Add any ethererum address
eth_exchange = OneInchExchange('0xA8eF29f7B7dA9163D529B1080701212122752c74')

# Grab available tokens
# test_response = eth_exchange.get_tokens() # works 
# 

# Try getting an exchange quote
exchange_response = eth_exchange.get_quote(from_token_symbol='ETH', to_token_symbol='BNT', amount=1)

pprint(exchange_response)