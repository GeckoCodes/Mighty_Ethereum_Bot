""" Script to find the common pairs between all exchanges
"""

# Imports
import requests
import json
from kyber_plugins import kyber_path
from python_1inch import OneInchExchange


def intersection_sets(sets):
    """ Function to find the intersection between a list of sets
    """
    intersection_set = {}
    for i in range(len(sets)):
        if i == 0:
            intersection_set = sets[i]
        else:
            intersection_set = intersection_set.intersection(sets[i])

    return intersection_set





#### UNISWAP ####

# Grab the list of uniswap tokens
with open("exploratory_scripts/uniswap_tokens.json", "r") as json_file:
    _ = json.load(json_file)
    tokens = _['tokens']

uniswap_tokens = set([x['symbol'] for x in tokens])

#### KYBER ####

# Get the Kyber Network Tokens
mainnet = "https://api.kyber.network/"

# Create the end point
kyber_path = kyber_path(mainnet, 'currencies', None)

# Perform the request and get the response
kyber_tokens = requests.get(kyber_path)

with open("exploratory_scripts/kyber_tokens.json", "r") as json_file:
    _ = json.load(json_file)
    tokens = _['data']

# Grab the Kyber tokens
kyber_tokens = set([x['symbol'] for x in tokens])

#### 1INCH ####

# Add any ethererum address
eth_exchange = OneInchExchange('0xA8eF29f7B7dA9163D529B1080701212122752c74')

# Grab available tokens
token_dict = eth_exchange.get_tokens() # works 

_1inch_tokens = set(token_dict.keys())


#### Find the common tokens ####
common_tokens = intersection_sets([uniswap_tokens, kyber_tokens, _1inch_tokens])

print("="*100)
print(f"Number of common tokens: {len(common_tokens)}")
print("="*100)

print(common_tokens)    




