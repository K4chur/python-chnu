def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))


with open('F1.txt', 'r') as f1, open('F2.txt', 'w') as f2:
    numbers = [int(line.strip()) for line in f1.readlines()]
    sorted_numbers = sorted(numbers, key=sum_of_digits)

    for num in sorted_numbers:
        f2.write(str(num) + '\n')


print("Sorting and writing to F2.txt is complete.")