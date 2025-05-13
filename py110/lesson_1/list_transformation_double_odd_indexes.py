# Try coding a solution that doubles the numbers that have odd indexes.

def double_odd_indexes(numbers):
    doubled_odd_indexes = []

    for i in range(len(numbers)):
        if i % 2 == 0:
            doubled_odd_indexes.append(numbers[i])
        else:
            doubled_odd_indexes.append(numbers[i] * 2)

    return doubled_odd_indexes

my_numbers = [1, 4, 3, 7, 2, 6]
print(double_odd_indexes(my_numbers))
print(my_numbers)