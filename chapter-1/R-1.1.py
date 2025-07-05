
def multiple(n, m):
    return isinstance(n, int) & isinstance(m, int) & (m % n == 0)

print(multiple(2, 4))   # n and m both are interger, m is mutliple of n, it will return true
print(multiple(3, 4))   # n and m both are interger not multiple, it will return false
print(multiple(2.5, 5)) # n as float 2.5 and m as 5, it will return false