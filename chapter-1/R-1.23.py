import array

try:
    list = eval(input("Enter your list: "))
    index = int(input("Enter your index: "))
    list[index] = 99
except IndexError:
    print("Don't try buffer overflow attacks in Python!")