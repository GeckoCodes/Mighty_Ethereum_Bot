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
        