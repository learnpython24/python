import string

def remove_punctuation(text):
    return ''.join(char for char in text if char not in string.punctuation)

sentence = "Let's try Mike."
cleaned = remove_punctuation(sentence)
print(cleaned)