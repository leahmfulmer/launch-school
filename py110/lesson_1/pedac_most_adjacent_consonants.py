# 1. For each string in the input list, determine the highest number of adjacent consonants within that string.

#### a. Initialize a helper function `is_consonant` which takes an input string `letter` as its parameter and returns a boolean object that describes whether or not that letter is a consonant.

def is_consonant(letter):
    return (letter not in 'aeiou')

#### b. Initialize a function `sort_by_consonant_count` which takes a list `my_list` as a parameter.

def sort_by_consonant_count(my_list):
    consonant_count = {}

    for i, string in enumerate(my_list):
        string_no_spaces = string.replace(' ', '')
        count = 0
 
        for j, letter in enumerate(string_no_spaces[:-1]):
            if is_consonant(string_no_spaces[j]) and is_consonant(string_no_spaces[j+1]):
                count += 1
            else:
                pass

            consonant_count[string] = count

# 2. Sort the input list (in descending order) based on on the number of consonants in each string.
    sorted_dict = dict(sorted(consonant_count.items(), reverse=True, key=lambda item: item[1]))

# 3. Return the sorted list.
    return list(sorted_dict.keys())

#### a. Iterate over all strings in the given list and return the keys of the dictionary `consonant_count` in order of most adjacent consonants to least.


# Example 1
my_list = ['aa', 'baa', 'ccaa', 'dddaa'] 
print(sort_by_consonant_count(my_list) == ['dddaa', 'ccaa', 'aa', 'baa']) 
# True

# Example 2
my_list = ['can can', 'toucan', 'batman', 'salt pan'] 
print(sort_by_consonant_count(my_list) == ['salt pan', 'can can', 'batman', 'toucan'])
# True

# Example 3
my_list = ['bar', 'car', 'far', 'jar'] 
print(sort_by_consonant_count(my_list) == ['bar', 'car', 'far', 'jar']) 
# True

# Example 4
my_list = ['day', 'week', 'month', 'year'] 
print(sort_by_consonant_count(my_list) == ['month', 'day', 'week', 'year'])
# True

# Example 5
my_list = ['xxxa', 'xxxx', 'xxxb'] 
print(sort_by_consonant_count(my_list) == ['xxxx', 'xxxb', 'xxxa']) 
# True