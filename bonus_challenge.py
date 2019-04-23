sentence = input('Please enter a sentence: ')

def word_summary(statement):
    split_statement = statement.split()
    histogram = {}
    for word in split_statement:
        if word not in histogram:
            histogram[word] = 1
        else:
            histogram[word] += 1
    return histogram

print(word_summary(sentence))