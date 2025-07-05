import array

def minmax(data):
    if len(data) < 2:
       raise ValueError("The sequence must contain at least two numbers.")
    min = max = data[0]
    for element in data:
        if min > element:
            min = element
        if element > max:
            max = element
    return (min, max)

print(minmax([1, 2 ,4, 23, 0, 3]))