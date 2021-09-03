import numpy as np

def non_linear_map(x, a=1, p=0.5):
    return a*(x/abs(x))*(abs(x))**p

def map_function(x, matrix):
    get_min_value = np.amin(matrix)
    get_max_value = np.amax(matrix)
    return 2*(x-get_min_value)/get_max_value-1


def inv_map_function(x):
    return (255)*((x+1)/2)