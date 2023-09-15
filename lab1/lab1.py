import math
import random


def first():
    n = int(input("Input n: "))
    m = int(input("Input m: "))

    while m == 0:
        m = int(input("Input number that is not zero: "))

    return round((math.sqrt(2) + math.sqrt((3 * n))) / (2 * m),3)


print(first())


def second():
    rand_value = random.randint(1, 100)
    while True:
        input_value = int(input("Enter a number from 1 to 100: "))
        if rand_value < input_value:
            print("My number is less than.")
        elif rand_value > input_value:
            print("My number is greater than.")
        else:
            print("You guessed it!")
            break


second()


def third(arr):
    minimum = min(arr)
    print("Min element in array:", minimum)

    sum_positive_odd = sum([x for x in arr if x > 0 and x % 2 != 0])
    print("Sum of positive odd numbers:", sum_positive_odd)

    positive_numb = [x for x in arr if x > 0]
    print("Positive numbers:", positive_numb)


array = [2, 5, -1, 8, 3, -4, 7, 10, 6, 1]
third(array)
