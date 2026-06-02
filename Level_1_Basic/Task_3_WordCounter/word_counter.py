from collections import Counter

f = 'words.txt'


def open_file(file):
    try:
        with open(file, 'r') as f:
            contents = f.read().split()
            return contents
    except FileNotFoundError:
        print('sorry, this file does not exist')
        return []


def word_counter(lst):
    word_counts = Counter(lst)
    return word_counts.most_common(10)


print(word_counter(open_file(f)))
