def simple_calculator():
    print("Simple Calculator (one input per line)")
    print("Enter numbers and operators (+, -, *, /, =)")
    print("Type 'C' to clear, 'Q' to quit")

    current_value = None
    pending_operator = None

    while True:
        user_input = input(">> ").strip()

        if user_input.lower() in ['q', 'quit']:
            print("Exiting calculator. Bye! 👋")
            break

        elif user_input.lower() in ['c', 'clear']:
            current_value = None
            pending_operator = None
            print("Screen: 0")
            continue

        elif user_input in ['+', '-', '*', '/']:
            if current_value is None:
                print("Error: No number entered yet.")
            else:
                pending_operator = user_input
            print(f"Screen: {current_value if current_value is not None else 0}")

        elif user_input == '=':
            print(f"Screen: {current_value if current_value is not None else 0}")

        else:
            try:
                num = float(user_input)
                if current_value is None:
                    current_value = num
                elif pending_operator:
                    if pending_operator == '+':
                        current_value += num
                    elif pending_operator == '-':
                        current_value -= num
                    elif pending_operator == '*':
                        current_value *= num
                    elif pending_operator == '/':
                        if num == 0:
                            print("Error: Division by zero.")
                            continue
                        current_value /= num
                    pending_operator = None
                else:
                    # Overwrite if no pending operation
                    current_value = num
                print(f"Screen: {current_value}")
            except ValueError:
                print("Invalid input. Enter a number or valid operator (+, -, *, /, =).")

# Run the calculator
simple_calculator()
