def decimal_to_binary(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"

    # Recursive case: divide n by 2 and convert the quotient to binary
    # Then, append the remainder (0 or 1) to the binary representation
    quotient = n // 2
    remainder = n % 2
    binary_representation = decimal_to_binary(quotient) + str(remainder)

    return binary_representation


# Input a decimal number
decimal_number = int(input("Enter a decimal number: "))

# Call the function to convert and print the binary representation
binary_result = decimal_to_binary(decimal_number)
print(f"The binary representation of {decimal_number} is: {binary_result}")