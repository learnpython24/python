
def sumofallsquare(n):
    if n <= 0:
       raise ValueError("n must be integer and more than zero")
    sum = 0
    for i in range(1, n):
        sum += i * i
    
    return sum

print(sumofallsquare(5))    