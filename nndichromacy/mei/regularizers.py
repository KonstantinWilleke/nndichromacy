from .utility import cumstom_initial_guess
from functools import partial

# Initial Guess
rgb_initial_guess = partial(cumstom_initial_guess, mean=111, std=60)
