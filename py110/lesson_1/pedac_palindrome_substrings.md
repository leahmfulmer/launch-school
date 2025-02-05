# PROBLEM
Given a string, write a function `palindrome_substrings` which returns all the palindromic substrings of the string that are 2 or more characters long. Palindrome detection should be case-sensitive.

### Test cases:

```python
# Comments show expected return values
palindrome_substrings("abcddcbA") # ["bcddcb", "cddc", "dd"]
palindrome_substrings("palindrome") # []
palindrome_substrings("") # []
palindrome_substrings("repaper") # ['repaper', 'epape', 'pap']
palindrome_substrings("supercalifragilisticexpialidocious") # ["ili"]
```

#### input: 
a string object
#### output:
a list object whose elements are strings
#### rules:
* **explicit requirements**:
    * every palindromic substring of 2 or more characters within the input string must be returned in a list (remember: palindromes are strings that read the same forward and backward)
    * palindrome detection must be case-sensitive
* **implicit requirements**:
    * if the input string is empty, return an empty list