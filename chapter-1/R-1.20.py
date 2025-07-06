import random

def custom_suffle(data):
    n = len(data)
    for i in range(n-1, 0, -1):
        j = random.randint(0, i)
        data[j], data[i] = data[i], data[j]

my_list = [1, 2, 3, 4, 5, 6]
custom_suffle(my_list)
print("Suffle list: ", my_list)