# Define the higher-order function for cumulative operations
def cumulative_operation(operation):
    def apply_operation(sequence):
        if not sequence:  # Check if the sequence is empty
            return 1  # Return 1 for an empty sequence, handling the factorial(0) case
        result = sequence[0]
        for element in sequence[1:]:
            result = operation(result, element)
        return result
    return apply_operation

# Implement factorial using the cumulative_operation function
factorial = lambda n: cumulative_operation(lambda x, y: x * y)(range(1, n + 1))

# Implement exponentiation using the cumulative_operation function
exponentiation = lambda base, exponent: cumulative_operation(lambda x, y: x * y)([base] * exponent)

# Test cases
print(factorial(5))  # Should print 120
print(exponentiation(2, 3))  # Should print 8
print(factorial(0))  # Should print 1, as 0! is defined as 1
print(factorial(1))  # Should print 1
print(factorial(6))  # Should print 720
print(exponentiation(3, 2))  # Should print 9 (3^2)
print(exponentiation(5, 0))  # Should print 1, as any number to the power of 0 is 1
print(exponentiation(2, 4))  # Should print 16 (2^4)
print(exponentiation(10, 3))  # Should print 1000 (10^3)