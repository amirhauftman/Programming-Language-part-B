fibonacci = lambda n: (lambda f, n: f(f, n, [0, 1]))(lambda self, n, a: a if n <= len(a) else self(self, n, a + [a[-1] + a[-2]]), n)[:n]

# Example usage:
n = 10
print(fibonacci(n))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
