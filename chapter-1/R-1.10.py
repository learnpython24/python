import array

def range_constructor(*input):
    start = 0
    end = 0
    step = 0
    if len(input) == 0:
        raise ValueError("Please check the input")
    elif len(input) == 1 and isinstance(input[0], int):
        start = input[0]
        i = 0
        while i < start:
            print(i)
            i += 1
    elif len(input) == 2 and isinstance(input[0], int) and isinstance(input[1], int):
        start = input[0]
        end = input[1]
        while start < end:
            print(start)
            start += 1
    elif len(input) == 3 and isinstance(input[0], int) and isinstance(input[1], int) and isinstance(input[2], int):
        start = input[0]
        end = input[1]
        step = input[2]
        while (start < end and step > 0) or (start > end and step < 0):
            print(start)
            start += step


range_constructor(8)
range_constructor(2, 8)
range_constructor(1, 8, 2)
range_constructor(50, 90, 10)
range_constructor(8, -10, -2)