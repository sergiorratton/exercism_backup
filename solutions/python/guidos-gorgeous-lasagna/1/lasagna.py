"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


# TODO: define the 'EXPECTED_BAKE_TIME' constant below.
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2
# TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    time_remaining = EXPECTED_BAKE_TIME - elapsed_bake_time
    return time_remaining


#TODO: Define the 'preparation_time_in_minutes()' function below.
# You might also consider defining a 'PREPARATION_TIME' constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations.

def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time (in minutes).

    :param number_of_layers: int - number of layers desired for the lasagna to have.
    :return: int - preparation time (in minutes) derived from 'PREPARATION_TIME'.

    Function that how many layers the lasagna must have as an argument and returns
    how much time was spent preparing the layers based on the 'PREPARATION TIME'.
    """
    prep_time = PREPARATION_TIME * number_of_layers
    return prep_time

# TODO: define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed time (in minutes).

    :param number_of_layers: int - number of layers that the lasagna has.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - time (in minutes) already spent in the whole lasagna baking process,
    derived from 'PREPARATION_TIME' and 'elapsed_bake_time'.

    Function that takes the actual minutes to prepare all the layers and adding it to
    the actual minutes the lasagna has been in the oven and returns how many minutes
    the whole process has been on.
    """
    elapsed_time = (PREPARATION_TIME * number_of_layers) + elapsed_bake_time
    return elapsed_time

# TODO: Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
