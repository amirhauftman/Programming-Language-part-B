# Python function using 5 nested lambda expressions
cumulative_sum_squares_even = lambda lists: list(map(
    lambda sublist: sum(
        map(lambda x: x**2, filter(lambda x: x % 2 == 0, sublist))
    ),
    lists
))

additional_test_cases = [
    [[10, 15, 20, 25], [30, 35, 40], [45, 50, 55]],
    [[2, 3, 4, 5, 6], [7, 8, 9, 10], [11, 12, 13, 14]],
    [[1, 2, 3, 4, 5, 6, 7, 8, 9], [], [10, 20, 30, 40]],
    [[0, 0, 0, 0], [1, 1, 1, 1], [2, 2, 2, 2]],
    [[-2, -4, -6], [2, 4, 6], [-1, 0, 1]]
]

for i, case in enumerate(additional_test_cases):
    result = cumulative_sum_squares_even(case)
    print(f"Additional Test case {i + 1}:")
    print(f"Input: {case}")
    print(f"Output: {result}")