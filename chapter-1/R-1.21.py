import array

def read_and_reverse():
    lines = []
    print("Enter text (press Ctrl+D end input on Linux/macOS, Ctrl+Z then Enter on Windows):)")

    try:
        while True:
            line = input()
            lines.append(line)
    except EOFError:
        print("\nReversed lines: ")
        for line in reversed(lines):
            print(line)

read_and_reverse()