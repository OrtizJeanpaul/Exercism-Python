"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""




EXPECTED_BAKE_TIME = 40

def bake_time_remaining(time_in_oven):
    """
    Calculate the bake time remaining.

    :param time_in_oven: int - The number of minutes the lasagna has been in the oven.
    :return: int - The number of minutes remaining to bake the lasagna.
    """
    return EXPECTED_BAKE_TIME - time_in_oven


def preparation_time_in_minutes(number_of_layers):
    """
    Calculate the preparation time in minutes for a given number of lasagna layers.

    Args:
        number_of_layers (int): The number of layers in the lasagna.

    Returns:
        int: The total preparation time in minutes, assuming each layer takes 2 minutes to prepare.
    """
    return number_of_layers * 2


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Calculate the total elapsed time in minutes for preparing and baking the lasagna.

    Args:
        number_of_layers (int): The number of layers in the lasagna.
        elapsed_bake_time (int): The time already spent baking the lasagna in minutes.

    Returns:
        int: The total elapsed time in minutes, including both preparation and baking time.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time


