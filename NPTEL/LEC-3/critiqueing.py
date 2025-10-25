def is_multiple(n: int, m: int) -> bool:
    """ Return True if n is a multiple of m , False otherwise.

    >>> is_multiple(10, 5)
    True
    >>> is_multiple(10, 0)
    False
    """
    if m == 0:
        return False

    return n % m == 0

print(is_multiple(10, 5))  # True
print(is_multiple(10, 0))  # False