import random

sentence = "I will never spam my friend again."

def introduce_typo(text):
    words = text.split()
    typo_type = random.choice(['replace', 'remove', 'duplicate', 'misspell'])
    index = random.randint(0, len(words) - 1)
    if typo_type == 'replace':
        word = list(words[index])
        if word:
            char_index = random.randint(0, len(word) - 1)
            word[char_index] = random.choice('abacdefghigkhijklmnopqrstuvwxyz')
            words[index] = ''.join(word)
    elif typo_type == 'remove':
        word = list(words[index])
        if len(word) > 1:
            del word[random.randint(0, len(word) - 1)]
            words[index] = ''.join(word)
    elif typo_type == 'duplicate':
        # Duplicate a word
        words.insert(index, words[index])
    elif typo_type == 'misspell':
        # Swap two letters in a word
        word = list(words[index])
        if len(word) > 1:
            i = random.randint(0, len(word) - 2)
            word[i], word[i+1] = word[i+1], word[i]
            words[index] = ''.join(word)

    return ' '.join(words)

# Pick 8 unique line numbers for typos
typo_lines = random.sample(range(1, 101), 8)
# Generate and print 100 lines
for i in range(1, 101):
    line = sentence
    if i in typo_lines:
        line = introduce_typo(sentence)
    print(f"{i}. {line}")
