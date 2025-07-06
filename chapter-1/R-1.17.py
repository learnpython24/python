import array

def scale(data, factor):
    for val in data:
        val *= factor

def correct_scale(data, factor):
    for i in range(len(data)):
        data[i] *= factor
 
lst = [1, 2, 3]
scale(lst, 10)
print(lst)
correct_scale(lst, 10)
print(lst)