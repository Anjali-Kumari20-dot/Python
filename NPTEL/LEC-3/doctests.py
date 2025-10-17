def to_fahrenheit(celsius):
    """ convert a given temperature in celcius to 
    fahrenheit , as low as it is above absolute zero.
    >>> to_fahrenheit(-300.0)
    nan
    """
    if celsius < -273.15:
        return float('nan')
    else:
        return (celsius * 9/5) + 32