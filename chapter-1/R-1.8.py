import array

def non_negative_index(string, negative_index):
    if len(string) < 1 & (negative_index > -1):
        raise ValueError("Input is nto correct")
    return len(string) + negative_index

string = "python"
print(non_negative_index(string, -3))
print("postive value: ", string[non_negative_index(string, -3)])
print("negative value: ", string[-3])
print(non_negative_index(string, -4))
print("postive value: ", string[non_negative_index(string, -4)])
print("negative value: ", string[-4])