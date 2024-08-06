# Lazy evaluation is a programming technique where the evaluation of an expression is delayed until its value is actually needed. In contrast to eager evaluation, which computes all values immediately, lazy evaluation avoids unnecessary computations and can improve efficiency by not computing values that are never used.

def generate_values():
    print('Generating values...')
    yield 1
    yield 2
    yield 3

def square(x):
    print(f'Squaring {x}')
    return x * x

print('Eager evaluation:')
values = list(generate_values())
squared_values = [square(x) for x in values]
print(squared_values)

print('\nLazy evaluation:')
squared_values = [square(x) for x in generate_values()]
print(squared_values)


# Lazy Evaluation:
# print('\nLazy evaluation:')
# squared_values = [square(x) for x in generate_values()]
# print(squared_values)

# [square(x) for x in generate_values()]: In this case, the generator function
# generate_values is passed directly into the list comprehension. The generator produces values
# on-the-fly as they are needed by the square function.

# The generator yields a value, which is then squared before the next value is generated. 
# This interleaves the generation and squaring of values, resulting in the following sequence:

# Generating values...
# Squaring 1
# Squaring 2
# Squaring 3

# and produces the list [1, 4, 9].

# The final output of the lazy evaluation block is:
# Lazy evaluation:
# Generating values...
# Squaring 1
# Squaring 2
# Squaring 3
# [1, 4, 9]

# Key Differences:
#     Eager Evaluation: The entire sequence of values is generated and stored in memory before
# any further processing (squaring) occurs. This results in all values being computed immediately,
# regardless of whether they are used later.

#     Lazy Evaluation: Values are generated and processed on demand. The generator yields values one at a time, 
# which are then squared immediately. 
# This avoids generating or processing values that are not needed and can save memory and computational resources.

# lazy evaluation delays the generation and computation of values until they are actually needed,
# which can lead to more efficient programs, especially when dealing with large data sets or computationally expensive operations.