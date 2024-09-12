# Example 1: Basic Syntax
# def say():
#     print('Output from say')

# print('First')
# say()
# print('Last')

# Example 2: Docstring Syntax
def say():
    """
    The say function prints "Hi!"
    """
    print('Hi!')

print('-' * 60)
print(say.__doc__)
print('-' * 60)
help(say)
