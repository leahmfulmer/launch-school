# Can you implement a `double_numbers` function that mutates its argument?

def double_numbers(numbers):
    for i, num in enumerate(numbers):
        numbers[i] = num * 2

    return numbers

my_numbers = [1, 4, 3, 7, 2, 6]
print(double_numbers(my_numbers))
print(my_numbers)