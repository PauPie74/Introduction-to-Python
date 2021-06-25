def max_rec(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        return max(numbers[0],max_rec(numbers[1:]))
