import array

def repeat_words(data):
    if len(data) == 0:
        raise ValueError("Given word list is empty")
    new_data = []
    for w in set(data):
        new_data.append((w, data.count(w)))
    return new_data

data = ["lion", "tiger", "dog", "lion", "dog"]

print(repeat_words(data))