def substrings(string):
    result = []
    start_index = 0

    while start_index <= len(string) - 2:
        num_chars = 2

        while num_chars <= len(string) - start_index:
            substring = string[start_index:start_index + num_chars]
            result.append(substring)
            num_chars += 1

        start_index += 1

    return result

def is_palindrome(string):
    reversed_string = string[::-1]
    return string == reversed_string

def palindrome_substrings(string):
    result = []
    substrings_list = substrings(string)

    for substring in substrings_list:
        if is_palindrome(substring):
            result.append(substring)

    return result

print(palindrome_substrings("abcddcbA")) # ["bcddcb", "cddc", "dd"]
print(palindrome_substrings("palindrome")) # []
print(palindrome_substrings("")) # []
print(palindrome_substrings("repaper")) # ['repaper', 'epape', 'pap']
print(palindrome_substrings("supercalifragilisticexpialidocious")) # ["ili"]
