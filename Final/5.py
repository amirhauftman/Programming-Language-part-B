from functools import reduce
print(reduce(lambda acc, x: acc + x, map(lambda x: x**2, filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6])), 0))

# Correctness: If the input list is empty or contains no even numbers, the reduce function in the previous solution would raise a TypeError because it would have no items to reduce. By providing an initial value of 0, we ensure that the function always returns a valid result (0 in this case) even if there are no elements to sum.
# Consistency with the original code: In the original code, sum_squared was initialized to 0 before the summation loop. Your solution maintains this behavior by starting the reduction with 0.
# Additionally, your use of acc (accumulator) as the first parameter in the reduce lambda function is a common and clear convention, making the code more readable.