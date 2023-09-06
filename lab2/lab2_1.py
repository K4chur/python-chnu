def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def compute_sum(x, a, epsi):
    sum_value = 0.0
    k = 0
    term = 1.0

    while abs(term) >= epsi:
        # Calculate the current term
        term = (((-1) ** k) * (x ** (-4 * k))) / ((a ** 4) * factorial(k))

        # Add the current term to the sum
        sum_value += term

        # Increment the term count
        k += 1

    return sum_value, k


x = float(input("Enter the value of x: "))
a = float(input("Enter the value of a: "))
epsi = float(input("Enter the precision ε: "))

sum_result, term_count = compute_sum(x, a, epsi)

print(f"The value of the sum with precision {epsi} = {sum_result}")
print(f"Number of terms included: {term_count}")


