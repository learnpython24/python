import array

def sum_of_odd_square(n):
    sum = 0
    for i in range(1, n):
        if i % 2 != 0:
            sum += i * i
    return sum

print(sum_of_odd_square(7))