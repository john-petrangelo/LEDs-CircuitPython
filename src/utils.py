"""
Collection of useful utility functions
"""


def map_value(value, in_min, in_max, out_min, out_max):
    """
    Map a value from one range to another.

    Parameters:
    - value (float): The input value to be mapped
    - in_min (float): The minimum value of the input range
    - in_max (float): The maximum value of the input range
    - out_min (float): The minimum value of the output range
    - out_max (float): The maximum value of the output range

    Returns:
    float: The mapped value in the output range
    """
    return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
