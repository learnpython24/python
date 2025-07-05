def divide_by_two(number):
    if number < 2:
        return "Given number is lesser than 2"
    count = 0
    while number >= 2:
        number = number / 2
        count += 1
    print("Number of times divided by 2 before result is less than 2:", count)
try:
    number = int(input("Enter a number: "))
    divide_by_two(number)
except ValueError:
    print("Given number is not valid")