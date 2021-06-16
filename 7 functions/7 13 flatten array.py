def flatten_array(array):
    if len(array) == 0:
        return array
    if isinstance(array[0], list):
        return flatten_array(array[0]) + flatten_array(array[1:])
    return array[:1] + flatten_array(array[1:])