# PY110 <span style="color:yellow">PEDAC</span> Guided Practice: Leftover Blocks

## Understand the <span style="color:yellow">P</span>roblem
### Inputs:
* A list object whose elements are all string objects.

### Outputs:
* A list object whose elements are the same string objects from the input list now sorted by number of adjacent consonants, most to least.

### Rules:
* Implicit:
    * Input and output should always be a single list of strings. No data types should be surprising here.
    * If two strings contain the same number of adjacent consonants, they should retain their original order in the output list.
    * Some strings may contain more than one word. 

* Explicit:
    * If two strings contain the highest number of adjacent consonants, they should retain their original order in the output list.
    * Consonants are considered adjacent if they are adjacent in a single word or stretched across two words and separated by a space (e.g., "Hellow world!").

### Questions:
* If adjacent consonants are stretched across two words and separated by punctuation, are they considered adjacent? E.g., "Hellow, world!", "Oh, dear. Read this."
* Does capitalization matter when determining if consonants are adjacent? E.g., "Mr. McCabb enjoys hot soup."
* Can strings be empty?
* Can strings contain multiple sentences?
* Is it possible for a string to contain no adjacent consonants?

## <span style="color:yellow">E</span>xamples and Test Cases
The following test cases are provided...

```python
# Example 1
my_list = ['aa', 'baa', 'ccaa', 'dddaa'] 
print(sort_by_consonant_count(my_list)) 
# ['dddaa', 'ccaa', 'aa', 'baa']

# Example 2
my_list = ['can can', 'toucan', 'batman', 'salt pan'] 
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

# Example 3
my_list = ['bar', 'car', 'far', 'jar'] 
print(sort_by_consonant_count(my_list)) 
# ['bar', 'car', 'far', 'jar']

# Example 4
my_list = ['day', 'week', 'month', 'year'] 
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

# Example 5
my_list = ['xxxa', 'xxxx', 'xxxb'] 
print(sort_by_consonant_count(my_list)) 
# ['xxxx', 'xxxb', 'xxxa']
```

Based on the examples above, we find that string elements may contain single words, or multiple words separated by a space. There is no punctuation in any of the string elements. No letters are capitalized, and no strings are empty. Strings may contain no adjacent consonants, and strings are sorted in decending order. The string(s) with the most adjacent consonants are listed first, and strings with progressively fewer adjacent consonants follow.

## <span style="color:yellow">D</span>ata Structures
The primary data structures at play here are lists and strings. Both input and output values are list objects whose elements are exclusively string objects. While sorting string elements based on adjacent consonants, we may employ a dictionary to keep track of all the given strings and their associated number of adjacent consonants. For example, 

```python
{
    'hello': 2,
    'world': 3,
    'string sleep': 4
}
```

## <span style="color:yellow">A</span>lgorithm



## Implement a Solution in <span style="color:yellow">C</span>ode
Refer to `pedac_most_adjacent_consonants.py` for this solution.