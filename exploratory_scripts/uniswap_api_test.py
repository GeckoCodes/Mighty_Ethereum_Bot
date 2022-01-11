""" Script to test the Uniswap API
"""


# # Need to set the Environment Variables
import os
os.environ['PROVIDER'] = 'https://mainnet.infura.io/v3/e35c185797154df0bc95fbcc5eaad31f'

from web3 import Web3
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/e35c185797154df0bc95fbcc5eaad31f'))


# Set up the uniswap environment
from uniswap import Uniswap

address = "0x0000000000000000000000000000000000000000"          # or "0x0000000000000000000000000000000000000000", if you're not making transactions
private_key = None # or None, if you're not going to make transactions
uniswap_wrapper = Uniswap(address, private_key, version=2)  # pass version=2 to use Uniswap v2


eth_address = '0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee'
dai_address = '0x6b175474e89094c44da98b954eedeac495271d0f'
mkr_address = '0x9f8f72aa9304c8b593d555f12ef6589cc3a579a2'

eth_checksum = w3.toChecksumAddress(eth_address)
dai_checksum = w3.toChecksumAddress(dai_address)
mkr_checksum = w3.toChecksumAddress(mkr_address)



print(uniswap_wrapper.get_eth_token_input_price(dai_checksum, 10**18)) # this worked
print(uniswap_wrapper.get_token_token_input_price(mkr_checksum, dai_checksum, 1000)) # this worked


# print(uniswap_wrapper.get_price_input(

# print(dir(get_token_token_input_price))