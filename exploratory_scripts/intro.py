"""
Script to test out some functionality around Ethereum programming with Python
"""
# Import the package
from web3 import Web3
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/e35c185797154df0bc95fbcc5eaad31f'))

# Need to set the Environment Variables
import os
os.environ['WEB3_INFURA_PROJECT_ID'] = "e35c185797154df0bc95fbcc5eaad31f"
os.environ['WEB3_INFURA_API_SECRET'] = "bf3aeb8dad8f42a9be2f6a61663455d2"

# Get the latest block information
from web3.auto.infura import w3
# print(w3.eth.get_block('latest'))

# Can get the balances of accounts - this is my Exodus wallet
balance = w3.eth.get_balance('0x5dA527EC74Ddf8af1495bF30072c5dD7b710dcFc')
print(f"I have {balance/10**18} Eth in my Wallet!!")