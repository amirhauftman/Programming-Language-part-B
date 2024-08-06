from functools import reduce
from functools import reduce
count_palindromes = lambda lists: list(map(lambda lst: reduce(lambda acc, x: acc + (x.replace(" ", "").lower() == x.replace(" ", "").lower()[::-1]), lst, 0), lists))
# Test cases for count_palindromes function
test_lists = [
    ["madam", "apple", "kayak", "banana"],
    ["level", "world", "radar", "python"],
    ["step on no pets", "no lemon, no melon", "card"],
    []
]

expected_results = [2, 2, 2, 0]

# Running the test cases
results = count_palindromes(test_lists)
print("Results:", results)
print("Expected:", expected_results)
print("Test Passed:", results == expected_results)