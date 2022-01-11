""" Script to test the Kyber network API
"""

# Imports
import requests
from pprint import pprint

# Define the main net end pointa
mainnet = "https://api.kyber.network/"

# Define extra params
currencies = "/currencies"

# Test call
response = requests.get(mainnet + currencies) # works

def kyber_path(mainnet, end_point, parameters: dict) -> str:
    """ Function to build the api path given a base url, end point and parameters

    """
    # Start building the path
    url_builder = mainnet

    # Add the end point
    url_builder += end_point

    # If we have parameters then need to add ?
    if not parameters:
        return url_builder
    else:
        # Add a ? then loop through and add the parameters
        url_builder += '?'

        # Build up the string
        for param, value in parameters.items():
            url_builder += param + '=' + value + '&'

        # Remove the final '&
        url_builder = url_builder[:-1]

    return url_builder
        


# Test the function
test_params = {
    'source' : '0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee',
    'dest'   : '0x6b175474e89094c44da98b954eedeac495271d0f',
    'sourceAmount': '1'
    }


# Build the url path 
url_out = kyber_path(mainnet, 'expectedRate', test_params)

# Grab the response
response = requests.get(url_out) # works

print(response.text)


