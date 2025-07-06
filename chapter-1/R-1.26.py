def check_formula(a, b, c):
    if a + b == c:
        print(f"{a} + {b} = {c}")
    elif a - b == c:
        print(f"{a} - {b} = {c}")
    elif a * b == c:
        print(f"{a} * {b} = {c}")
    elif b != 0 and a / b == c:
        print(f"{a} / {b} = {c}")
    elif a == b + c:
        print(f"{a} = {b} + {c}")
    elif a == b - c:
        print(f"{a} = {b} - {c}")
    elif a == b * c:
        print(f"{a} = {b} * {c}")
    elif c != 0 and a == b / c:
        print(f"{a} = {b} / {c}")
    else:
        print("No valid arithmetic formula found.")

# Get input from the user
try:
    a = int(input("Enter integer a: "))
    b = int(input("Enter integer b: "))
    c = int(input("Enter integer c: "))
    check_formula(a, b, c)
except ValueError:
    print("Please enter valid integers.")
