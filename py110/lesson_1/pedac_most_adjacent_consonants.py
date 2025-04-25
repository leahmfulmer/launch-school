# 1. For each string in the input list, determine the highest number of adjacent consonants within that string.

#### a. Initialize a helper function `is_vowel` which takes an input string `letter` as its parameter and returns a boolean object that describes whether or not that letter is a vowel.

def is_vowel(letter):
    return (letter in ('a', 'e', 'i', 'o', 'u'))

#### b. Initialize a function `sort_by_consonant_count` which takes a list `my_list` as a parameter.

def sort_by_consonant_count(my_list):

#### c. Initiate the empty dictionary `consonant_count`.
    consonant_count = {}

#### d. Begin a `for` loop which iterates over each string in the input list. Initialize the variable `count` and set it equal to 0.
    for string in my_list:
        count = 0

#### e. Begin a nested `for` loop which iterates over each letter and invoke the helper function `is_vowel` to evaluate if the current letter is a vowel. If the current letter is not a vowel, increment `count` by 1. If the current letter is a vowel, set `count` back to 0. Before completing the iteration, add an element to `consonant_count` with the current word as its key and the integer object referenced by the variable `count` as its value. NOTE: Implement a comparison where the largest value of `count` is retained.
        for letter in string:
            if is_vowel(letter):
                count = 0
            else:
                count += 1

            consonant_count[string] = count

# 2. Sort the input list (in descending order) based on on the number of consonants in each string.

# 3. Return the sorted list.

#### a. Iterate over all strings in the given list and return the keys of the dictionary `consonant_count` in order of most adjacent consonants to least.
