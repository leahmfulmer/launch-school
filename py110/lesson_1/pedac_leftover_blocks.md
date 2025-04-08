# PY110 PEDAC Guided Practice: Leftover Blocks

## Understand the Problem
### Inputs:
* The number of available blocks (integer object).

### Outputs:
* The number of blocks left over after building the tallest valid structure (integer object).

### Rules:
* Implicit:
    * We're building a square pyramid.
    * The top row will contain 1 block, the next will contain 4 blocks, then 9 blocks, 25, etc. The number of blocks in each layer is the square of the row number, beginning with row 1 as the top layer.

* Explicit:
    * The building blocks are cubes.
    * A valid structure is built in layers. The top layer is a single block, and every block is supported by 4 blocks in the layer beneath it. Blocks in a base layer may support more than one block above them, but there may not be gaps between blocks.

### Questions:
* Will the input value always be an integer object? Ought we handle exceptions around input values or types?
* **Suggested:** Does a valid base layer potentially contain more blocks than it requires (e.g., more than four blocks supporting a block in the layer above)?
* **Suggested:** Will there *always* be blocks left over, or could the number of leftover blocks be 0?

## Examples and Test Cases
The following test cases are provided...

```python
print(calculate_leftover_blocks(0) == 0)   # True
print(calculate_leftover_blocks(1) == 0)   # True
print(calculate_leftover_blocks(2) == 1)   # True
print(calculate_leftover_blocks(4) == 3)   # True
print(calculate_leftover_blocks(5) == 0)   # True
print(calculate_leftover_blocks(6) == 1)   # True
print(calculate_leftover_blocks(14) == 0)  # True
```

From these test cases, I believe we can assume that the input value will always be an integer object. There is no need to handle exceptions around unexpected input value. Further, valid layers ought not to include any more blocks than are required. Lastly, the number of leftover blocks can be 0, so there will not always be blocks left over.

## Data Structures
The primary data structure at play here is the integer object. The input and output values are both represented by integers, and the arithmetic involved with the number of blocks will surrounded integer addition. For the structure, we may need to use a list to represent the number of blocks in a valid layer.

## Algorithm

1. Within the function `calculate_leftover_blocks`, initialize the variables `current_row` and `sum_of_blocks` to represent the current row number and the sum of blocks already used to create the valid structure, respectively.
2. Use a while loop to compare the current `sum_of_blocks` to the intger referenced by `total_blocks`. If `total_blocks` is greater than the `sum_of_blocks`, add the number of blocks in the next layer to `sum_of_blocks`. Then increment the `current_row`.
3. If the input integer exceeds the current `sum_of_blocks`, break the while loop. Calculate and return the number of remaining blocks to the function invocation.

## Implement a Solution in Code
Refer to `pedac_leftover_blocks.py` for this solution.