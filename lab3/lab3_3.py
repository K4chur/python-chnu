def count_previous_occurrences(text):
    words = text.split()
    word_count = {}
    result = []

    for word in words:
        if word not in word_count:
            word_count[word] = 0

        result.append(word_count[word])
        word_count[word] += 1

    return result


input_text = """
one two one two three
She sells sea shells on the sea shore;
The shells that she sells are sea shells I’m sure.
So if she sells sea shells on the sea shore,
I’m sure that the shells are sea shore shells.
"""


result = count_previous_occurrences(input_text)
for count in result:
    print(count, end=" ")