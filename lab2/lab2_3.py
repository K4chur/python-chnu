def remove_duplicates(text):
    # Split the text into words using spaces and punctuation marks as separators
    words = text.split()

    # Create an empty list to store unique words
    unique_words = []

    # Iterate through each word and add it to unique_words if it hasn't been added already
    for word in words:
        if word not in unique_words:
            unique_words.append(word)

    # Join the unique words back into text, separated by spaces
    new_text = ' '.join(unique_words)

    return new_text

input_text = input("Enter the text: ")
result = remove_duplicates(input_text)

print("Text without duplicate words:")
print(result)