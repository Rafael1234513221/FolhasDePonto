"""Descobre o fatorial de um número n."""

def fatorial(n):
    """
    Dado um número n, é retornado seu devido fatorial.
    """
    a = 1
    total = 1
    while a != n:
        total += a * total
        a += 1
    return total

print(fatorial(500))
