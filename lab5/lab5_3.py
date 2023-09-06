import matplotlib.pyplot as plt
import re

text = """
This is a regular sentence.
Can i ask u somthing?
BUT this is also regular sentence.
What time is it?
I may be silent.
Wow, that's amazing!
The quick brown fox jumps over the lazy dog...
"""


def count_sentence_types(text):
    sentences = re.split(r'(?<=[.!?])\s+', text)
    sentence_types = {
        'Regular': 0,
        'Question': 0,
        'Exclamation': 0,
        'Ellipsis': 0
    }

    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence:
            continue
        if sentence[-1] == '?':
            sentence_types['Question'] += 1
        elif sentence[-1] == '!':
            sentence_types['Exclamation'] += 1
        elif sentence[-3:] == '...':
            sentence_types['Ellipsis'] += 1
        else:
            sentence_types['Regular'] += 1

    return sentence_types


sentence_counts = count_sentence_types(text)

sentence_types = list(sentence_counts.keys())
counts = list(sentence_counts.values())


plt.figure(figsize=(10, 6))
plt.bar(sentence_types, counts)
plt.xlabel('Sentence Types')
plt.ylabel('Frequency')
plt.title('Sentence Type Frequency Histogram')

plt.savefig('5_3.png')

plt.show()

