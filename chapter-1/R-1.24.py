import string

def count_vowels(text):
    vowels = ['a', 'e', 'o', 'i', 'u']
    return len([char for char in text if char in vowels])

try:
    text = input("Enter your string: ")
    print(count_vowels(text.lower()))
except ValueError:
    print("Input is empty string.")