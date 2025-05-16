# Try coding a function that lets you multiply every list element by a specifed value. As with `double_numbers`, don't mutate the list, but return a new list instead.

def multiply(numbers, factor):
    multiplied_numbers = []

    for i in range(len(numbers)):
        multiplied_numbers.append(numbers[i] * factor)

    return multiplied_numbers

my_numbers = [1, 4, 3, 7, 2, 6]
print(multiply(my_numbers, 3))
print(my_numbers)