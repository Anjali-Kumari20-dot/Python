def max_positive_integer(data: list) -> int:
    positives = [x for x in data if isinstance(x, int) and x > 0]
    return max(positives) if positives else 0
