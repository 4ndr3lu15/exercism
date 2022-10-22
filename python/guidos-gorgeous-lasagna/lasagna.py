"""
Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(t):
	"""
	Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
	return EXPECTED_BAKE_TIME - t

def preparation_time_in_minutes(n):
	"""
    Return preparation time.

    This function takes a number representing the number of layers  and calculates the time spent preparing the lasagna.
    """
	return n * PREPARATION_TIME

def elapsed_time_in_minutes(n, a):
	"""
    Return elapsed cooking time.

    This function takes two numbers representing the number of layers & the time already spent 
    baking and calculates the total elapsed minutes spent cooking the lasagna.
    """
	return preparation_time_in_minutes(n) + a
	
