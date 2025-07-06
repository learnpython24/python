def factors(n):
    """Generate all factors of n in increasing order."""
    small = []
    large = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            small.append(i)
            if i != n // i:
                large.append(n // i)
    for factor in small:
        yield factor
    for factor in reversed(large):
        yield factor

for f in factors(100):
    print(f, end=' ')