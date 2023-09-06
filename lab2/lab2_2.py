def find_term(x, epsi):
    a_n_minus_1 = x  # Initialize a_0 as x
    a_n = a_n_minus_1  # Initialize a_n as a_0

    for n in range(1, 100):
        a_n = (4 / 5) * a_n_minus_1 + (x / (5 * (a_n_minus_1 ** 4)))

        # Check the condition |a_n - a_{n-1}| < ε
        if abs(a_n - a_n_minus_1) < epsi:
            return a_n, n

        a_n_minus_1 = a_n

    return None, None  # If the condition is not met for the first 100 terms


x = float(input("Enter the value of x: "))
epsi = float(input("Enter the value of ε: "))

result, position = find_term(x, epsi)

if result is not None:
    print(f"The first term a_n that satisfies |a_n - a_n-1| < ε is {result}")
    print(f"Its position in the sequence is n = {position}")
else:
    print("The condition |a_n - a_n-1| < ε is not met for the first 100 terms.")