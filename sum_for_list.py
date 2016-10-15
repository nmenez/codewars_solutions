from collections import Iterable


def factorization(n):
    factors = [d for d in range(1, n // 2 + 1) if n // d == n / d]
    factors.remove(1)
    return factors


def isprime(n):
    if n in (1, 2):
        return True
    for d in range(2, n // 2 + 1):
        if n // d == n / d:
            return False
    return True


def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x, ignore_types)
        else:
            yield x


def primefactorization(n):
    if n<0: n=abs(n)
    if isprime(n):
        return set([n])
    else:
        return set(list(flatten([primefactorization(d)
                                 if isprime(d)
                                 else primefactorization(d)
                                 for d in factorization(n)])))


def sum_for_list(lst):
    n_factor = [(n, primefactorization(n)) for n in lst]
    all_factors = set()
    for n, factors in n_factor:
        all_factors.update(factors)

    res  = [[f, sum([n for n, factors in n_factor if f in factors])] for f in all_factors]
    res = sorted(res, key=lambda x: x[0])
    return res


print(primefactorization( -45))
print(sum_for_list([107, 158, 204, 100, 118, 123, 126, 110, 116, 100]
))
