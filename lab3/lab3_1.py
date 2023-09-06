def is_symmetric(sequence):
    return sequence == sequence[::-1]

def build_vector(matrix):
    n = len(matrix)
    vector = []

    for row_number in range(n):
        row = matrix[row_number]
        if is_symmetric(row):
            vector.append(row_number)

    return vector

matrix = [
    [1, 2, 3, 3, 2, 1],
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 3, 2, 1],
    [7, 8, 9, 9, 8, 7]
]

symmetric_vector = build_vector(matrix)

print(symmetric_vector)

for col in symmetric_vector:
    print(matrix[col])