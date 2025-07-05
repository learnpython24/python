def make_change(charged, given):
    change = given - charged

    if change < 0:
        return "Insufficient payment."
    elif change == 0:
        return "No change return."
    
    denominations = [
        (100.00, "hundred-dollar bill"),
        (50.00, "fifty-dollar bill"),
        (20.00, "twenty-dollar bill"),
        (10.00, "ten-dollar bill"),
        (5.00, "five-dollar bill"),
        (1.00, "one-dollar bill"),
        (0.25, "quarter"),
        (0.10, "dime"),
        (0.05, "nickel"),
        (0.01, "penny")
    ]

    change_cents = round(change * 100)
    result = {}
    for value, name in denominations:
        value_cents = round(value * 100)
        if change_cents >= value_cents:
            count = change_cents // value_cents
            result[name] = count
            change_cents = count * value_cents
    
    output = []
    for denomination, count in result.items():
        if count > 1:
            # Handle plural forms
            if denomination == "penny":
                output.append(f"{count} pennies")
            elif denomination.endswith("y"):
                output.append(f"{count} {denomination[:-1]}ies")
            else:
                output.append(f"{count} {denomination}s")
        else:
            output.append(f"{count} {denomination}")
    
    return "\n".join(output)

# Get user input
try:
    charged = float(input("Enter the amount charged: $"))
    given = float(input("Enter the amount given: $"))
    
    print("\nChange breakdown:")
    print(make_change(charged, given))
except ValueError:
    print("Please enter valid monetary amounts.")
