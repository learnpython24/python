
def calculator():
    print("🔢 Handheld Calculator")
    print("Type numbers and operations like on a calculator.")
    print("Type 'C' to clear, 'Q' to quit.")
    print("Example: 5, +, 3, =")

    current = 0
    operator = None
    waiting_for_operand = False

    while True:
        button = input(">> ").strip()

        if button.lower() in ['q', 'quit']:
            print("👋 Exiting calculator.")
            break

        elif button.lower() in ['c', 'clear']:
            current = 0
            operator = None
            waiting_for_operand = False
            print("Screen: 0")

        elif button in ['+', '-', '*', '/']:
            operator = button
            waiting_for_operand = True

        elif button == '=':
            print(f"Screen: {current}")

        else:
            try:
                num = float(button)
                if operator and waiting_for_operand:
                    if operator == '+':
                        current += num
                    elif operator == '-':
                        current -= num
                    elif operator == '*':
                        current *= num
                    elif operator == '/':
                        if num == 0:
                            print("Error: Division by zero.")
                            continue
                        current /= num
                    waiting_for_operand = False
                else:
                    current = num
                print(f"Screen: {current}")
            except ValueError:
                print("Invalid input. Use numbers, +, -, *, /, =, C, or Q.")

calculator()