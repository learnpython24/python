import array

def correct_scale(data, factor):
    for i in range(len(data)):
        data[i] *= factor
 
lst = [1, 2, 3]
correct_scale(lst, 10)
print(lst)