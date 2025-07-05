import array

def list_of_2(number):
    # list = []
    # for i in range(number):
    #     list.append(2 ** i)
    # return list
    return [2 ** i for i in range(number)]

print(list_of_2(9))