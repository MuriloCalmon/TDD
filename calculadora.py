def soma(a , b):
    """Soma a e b
    
    >>> soma(10, 20)
    30

    >>> soma(-10, 20)
    10

    >>> soma('10', 100)
    Traceback (most recent call last):
    ...
    AssertionError: a precisa ser int ou float
    """
    assert isinstance(a, (int, float)), 'a precisa ser int ou float'
    assert isinstance(b, (int, float)), 'b precisa ser int ou float'
    return a + b

def subtrai(a, b):
    """Subtrai a e b

    >>> subtrai('10', 5)
    Traceback (most recent call last):
    ...
    AssertionError: a precisa ser int ou float
    """
    assert isinstance(a, (int, float)), 'a precisa ser int ou float'
    assert isinstance(b, (int, float)), 'b precisa ser int ou float'
    return a - b

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)