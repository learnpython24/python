import array

def has_odd_product_pair(sequence):
    if len(sequence) == 0:
        raise ValueError("Please check input")
    odds = []
    for i in sequence:
       if i % 2 == 1:
           odds.append(i)
    if len(odds) > 1:
        return odds[0] * odds[1]

print(has_odd_product_pair(list(range(2, 8))))