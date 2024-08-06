concat = lambda l: l[0] if len(l) == 1 else l[0] + ' ' + concat(l[1:])

# Test cases
print(concat(["Hello", "world"]))
print(concat(["Python", "is", "awesome"]))
print(concat(["One"]))
print(concat(["", "Empty", "strings", "too"]))

#another solution
# concat = lambda l: (lambda f, l: f(f, l))(lambda self, l: l[0] if len(l) == 1 else l[0] + ' ' + self(self, l[1:]), l)

# # Test cases
# print(concat(["Hello", "world"]))                # Output: "Hello world"
# print(concat(["Python", "is", "awesome"]))       # Output: "Python is awesome"
# print(concat(["One"]))                           # Output: "One"
# print(concat(["", "Empty", "strings", "too"]))   # Output: " Empty strings too"
