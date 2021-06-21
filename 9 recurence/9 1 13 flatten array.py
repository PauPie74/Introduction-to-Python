def flatten_array(array):
    if isinstance(array, list):
        if len(array) == 0:
            return []
        n, r = array[0], array[1:]
        return flatten_array(n) + flatten_array(r)
    else:
        return [array]