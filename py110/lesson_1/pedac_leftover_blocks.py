# Function definition
def calculate_leftover_blocks(total_blocks):
    # 1. Within the function `calculate_leftover_blocks`, initialize the variables `current_row` and `sum_of_blocks` to represent the current row number and the sum of blocks already used to create the valid structure, respectively.
    current_row = 0
    sum_of_blocks = 0

    # 2. Use a while loop to compare the current `sum_of_blocks` to the intger referenced by `total_blocks`. If `total_blocks` is greater than the `sum_of_blocks`, add the number of blocks in the next layer to `sum_of_blocks`. Then increment the `current_row`.
    while sum_of_blocks <= total_blocks:
        sum_of_blocks += (current_row + 1)**2
        current_row += 1

    # 3. If the input integer exceeds the current `sum_of_blocks`, break the while loop. Calculate and return the number of remaining blocks to the function invocation.
    sum_of_blocks -= (current_row)**2
    return total_blocks - sum_of_blocks


# Test cases
print(calculate_leftover_blocks(0) == 0)   # True
print(calculate_leftover_blocks(1) == 0)   # True
print(calculate_leftover_blocks(2) == 1)   # True
print(calculate_leftover_blocks(4) == 3)   # True
print(calculate_leftover_blocks(5) == 0)   # True
print(calculate_leftover_blocks(6) == 1)   # True
print(calculate_leftover_blocks(14) == 0)  # True
