import matplotlib.pyplot as plt
from collections import Counter

text = "This is a sample text for creating a letter frequency histogram."

letters = list(text.lower())

letter_counts = Counter(letters)

letters, counts = zip(*letter_counts.items())

plt.figure(figsize=(10, 6))
plt.bar(letters, counts)
plt.xlabel('Letters')
plt.ylabel('Frequency')
plt.title('Letter Frequency Histogram')

plt.savefig('5_2.png')

plt.show()

