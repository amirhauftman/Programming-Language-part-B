# One-line function to get sorted prime numbers in descending order
prime_sort = lambda nums: sorted(
    [n for n in set(nums) if n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))], 
    reverse=True
)

# Test cases
assert prime_sort([10, 7, 5, 24, 11, 3]) == [11, 7, 5, 3], "Test 1 Failed"
assert prime_sort([2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == [29, 23, 19, 17, 13, 11, 7, 5, 3, 2], "Test 2 Failed"
assert prime_sort([4, 6, 8, 10]) == [], "Test 3 Failed"
assert prime_sort([]) == [], "Test 4 Failed"
assert prime_sort([31, 37, 41, 43, 47, 53, 59]) == [59, 53, 47, 43, 41, 37, 31], "Test 5 Failed"
assert prime_sort([7, 7, 5, 3, 3, 2, 2]) == [7, 5, 3, 2], "Test 6 Failed"

print("All tests passed!")
