word = input('Please enter a word: ')

def letter_histogram():
    histogram = {}
    for letter in word:
        if letter not in histogram:
            histogram[letter] = 1
        else:
            histogram[letter] += 1
    return histogram

print(letter_histogram())