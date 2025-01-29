# PY 109 Study Guide: Python Basics

Just for fun, here is a summary of all Python data types...
| Type | Class | Category | Primitive? | Mutable? |
| :--- | :--- | :--- | :--- | :--- |
| integers | `int` | numerics | primitive | immutable |
| floats | `float` | numerics | primitive | immutable |
| strings | `str` | text sequences | primitive | immutable |
| booleans | `bool` | booleans | primitive | immutable |
| lists | `list` | sequences | non-primitive | mutable |
| tuples | `tuple` | sequences | non-primitive | immutable |
| ranges | `range` | sequences | non-primitive | immutable |
| dictionaries | `dict` | mappings | non-primitive | mutable |
| sets | `set` | sets | non-primitive | mutable |
| frozensets | `frozenset` | sets | non-primitive | immutable |
| functions | `function` | functions | non-primitive | mutable |
| `None` | `NoneType` | nulls | inconclusive | immutable |


## naming convention: legal vs. idiomatic, illegal vs. non-idiomatic

In Python, legal naming conventions are those which are allowed by Python's syntax (i.e., they can be used without raising an error). Legal names...
* begin with a letter or underscore
* contain only letters, numbers, and underscores
* are not any of Python's reserved keywords (e.g., `if`, `while`, `def`)<br><br>


Illegal naming conventions are those which violate Python's syntax; they will raise a `SyntaxError` or do something unexpected if used. Illegal names...
* begin an identifier with a digit
* include spaces or other non-alphabetic, non-underscore characters
* use one of Python's reserved keywords<br><br>


Idiomatic naming conventions are those which are both legal and in alignment with the conventions defined by the Python programming community. Using idiomatic naming conventions makes one's code readable to other Python programmers and demonstrates a knowledge of Python best practices. Idiomatic names include...
* variables and functions defined with `snake_case`: all lowercase with underscore-separated words
* constants defined with `SCREAMING_SNAKE_CASE`: all uppercase with underscore-separated words
* classes defined with `PascalCase`: each word capitalized with no separation between words<br><br>


Non-idomatic naming conventions are allowed by Python's syntax, but they violate Python community conventions. Using non-idiomatic naming conventions may make one's code confusing to other Python programmers or demonstrate ignorance of Python best practices. Examples of non-idiomatic names include...
* a variable named `MY_VARIABLE`
* a class that uses `camelCase` 
* any surprising mix of cases: `tHis_iS_My_VarIAbLe`<br><br>

## type coercions: explicit (e.g., using `int()`, `str()`) and implicit

Type coercion involves changing an object value from one data type to another. This can happen explicitly with constructor function...
* `int()`, `float()`, `str()`, `list()`, `dict()`, `tuple()`, `set()`, `frozenset()` convert objects to integers, floats, strings, lists, dictionaries, tuples, sets, and frozensets, respectively.<br><br>

Or it can happen implicitly in a variety of ways:
* Mathematical statements involving plain division may convert to a `float`: `5 / 2 = 2.5`
* Mathematical statements involving type mixing may convert to a `float`: `4 + 2.0 = 6.0`
* Invoking the `print()` function implicitly converts all input to a string object before printing.<br><br>

## numbers
There are several types of numbers in Python; the ones we primarily consider in Launch School are integers (`int`) and floats (`float`). Integers are whole numbers and do not include a decimal point. Floats are real numbers and always include a decimal point, even if there is not decimal value. Both integers and floats are immutable, primitive data types.

* `int`: `1`, `-1`
* `float`: `1.0`, `-1.0`, `12.34`<br><br>

With respect to large numbers, one may represent commas with underscores:
* `1000 == 1_000` returns `True`
* `123.456_789 == 123.456789` returns `True`<br><br>

Furthermore, one may represent large floats with scientific notation, but large integers are never represented with scientific notation:
* `print(float(3e16))` returns `3e16`
* `print(int(3e16))` returns `30000000000000000`<br><br>

One thing to note is that floating point numbers contain **imprecision**. Floating point numbers are stored in binary format, which cannot precisely represent many decimals using only powers of two. Some values become recurring decimals in binary, and thus cannot be completely represented with limited data storage. This may cause unexpected errors; use `math.isclose()`.

```python
print(0.1 + 0.2 == 0.3)         # False

import math
math.isclose(0.1 + 0.2, 0.3)    # True
```

## strings
Strings are immutable, primitive text sequences. They can be represented with single quotes (`'hi'`), double quotes (`"hello"`), or triple single quotes (`'''`) or triple double quotes (`"""`)for multi-line strings. If a quote contains both single and double quotes in its body, you may use triple quotes or escape characters:
* `'''What d'you mean by "closed"?'''`
* `"What d'you mean by \"closed\"?"`<br><br>

In many cases, strings share the same behavior as sequences. They can be...
* indexed: `'hello'[0] == 'h'` returns `True`; `'hello'[-4] == 'e'` returns `True`
* sliced: `'hello'[0:2] == 'he'` returns `True`; `'hello'[::2] == 'hlo'` returns `True`<br><br>

## f-strings
Formatted string literals, or f-strings, allow for an operation called string interpolation in which string literals are embedded with expressions. If you want to use literal burly brackets in your string, just double them up!
```Python
age = 30
print(f"Use {{age}} to embed an expression. Today I'm {age} years old!")
# Use {age} to embed an expression. Today I'm 30 years old!
```

They can also be used to format numbers.
```Python
my_number = 1234.5678
print(f'{my_number:,}')    # 1,234.5678
print(f'{my_number:_}')    # 1_234.5678
```

## string methods
As immutable objects, strings cannot be mutated under any circumstances. However, string methods can be performed on strings, returning a new string object with the intended modifications.<br><br>

### `str.capitalize()`
Returns a copy of `str` with the first letter capitalized and the remaining letters in lowercase.<br><br>

### `str.swapcase()`
Returns a copy of `str` with cases completely swapped: lowercase characters becomes uppercase and uppercase characters become lowercase.<br><br>


### `str.upper()`
Returns a copy of `str` with all characters in uppercase.<br><br>

### `str.lower()`
Returns a copy of `str` with all characters in lowercase.<br><br>

### `str.isalpha()`
Returns `True` if all characters in `str` are alphabetic, or `False` if any character is non-alphabetic. *Note:* Python is aware of all Unicode characters, even those that are not in English. To include only ascii characters, use `str.isalpha() and str.isascii()`.<br><br>

### `str.isdigit()`
Returns `True` if all characters in `str` are digits, or `False` if any character is not a digit.<br><br>

### `str.isalnum()`
Returns `True` if all characters in `str` are alphabetic or digits, or `False` if any character is neither alphabetic nor a digit.<br><br>

### `str.islower()`
Returns `True` if all characters in `str` are lowercase, or `False` if any character is not lowercase.<br><br>

### `str.isupper()`
Returns `True` if all characters in `str` are uppercase, or `False` if any character is not uppercase.<br><br>

### `str.isspace()`
Returns `True` if all characters in `str` are whitespace characters, including space (`' '`), newline (`'\n'`), tab (`'\t'`), carriage return (`'\r'`), vertical tab (`'v'`), and form feed (`'f'`), as well as foreign whitespace characters, or `False` where this is not the case.<br><br>

### `str.strip('characters')`
Returns a copy of `str` with leading and trailing whitespace characters removed. This method can take an argument such as `str.strip('+')` to remove all leading and trailing instances of those characters from the copied string. *Note:* This method removes characters, not substrings.
```Python
my_string = 'abbcccxyzaaabbc'
my_string.strip('abc')           # 'xyz'
```

### `str.rstrip('characters')`
Returns a copy of `str` with trailing whitespace (default) or chosen characters removed.<br><br>

### `str.lstrip('characters')`
Returns a copy of `str` with leading whitespace (default) or chosen characters removed.<br><br>

### `str.replace('old', 'new')`
Returns a copy of `str` with the first argument replaced by the second argument.
```Python
my_string = 'cat'
my_string.replace('c', 'h')    # 'hat'
```

### `str.split('character')`
Returns a list of the words in `str`, using spaces as an indicator of a new word, or a given character.
```Python
my_string = 'I love you'
print(my_string.split())            # ['I', 'love', 'you']

my_next_string = 'I + love + you'
print(my_next_string.split('+'))    # ['I ', ' love ', ' you']
```

### `str.find('string')`
Returns the first index at which the given substring is found within `str`, searching from left to right.<br><br>

### `str.rfind('string')`
Returns the first index at which the given substring is found within `str`, searching from right to left. *Note:* This method returns the left-to-right index of `str`, even though it searches for the given input from right to left.<br><br>

## boolean vs. truthiness
Booleans are immutable, primitive objects representing binary states. There are two boolean values: `True` and `False`. They often appear as the return value of methods or logical / comparison operations. In mathematical expressions, `True` evaluates to `1` and `False` evaluates to `0`.

Truthiness is a way of describing how a value behaves in a Boolean context. When an object contains a non-zero or non-empty value, we say that that value "is truthy" or "evaluates to true". When the object contains a zero, empty, or `None` value, we say that that value "is falsy" or "evaluates to false". Examples of falsy values include:
* `False`, `None`
* `0`, `0.0`, and other numerical representations of zero
* empty (text) sequences: `""`, `[]`, `()`, `{}`, `range(0)`, `set()`, `frozenset()`
* any custom data types defined as falsy<br><br>


## `None`
`None` is an immutable data type used to describe an object with an absent value. The default return value for custom functions, as well as many methods that mutate mutable objects is `None`. Launch School is inconclusive about whether `None` is a primitive or non-primitive data type.<br><br>

## ranges
Ranges are immutable, non-primitive sequences that increment integer values from one endpoint to another. Ranges are "lazy sequences" meaning that they do not create element values until they are called, usually by iterating them in a `for` loop or coercing them into another data type,. Their syntax is `range(inclusive_starting_integer, exclusive_ending_integer, step_size)`. Make a decending range by inputing a negative step size and a startpoint greater than the endpoint. If the step size is negative and the startpoint is less than the endpoint, or if the startpoint is equal to the endpoint no matter the step size, Python will return an empty range.
```Python
print(range(2, 25, 4))            # range(2, 25, 4)
print(list(range(2, 25, 4)))      # [2, 6, 10, 14, 18, 22]

print(range(1, 10, -1))           # range(1, 10, -1)
print(list(range(1, 10, -1)))     # []

print(range(10, 10, -1))          # range(10, 10, -1)
print(list(range(10, 10, -1)))    # []
```

## list and dictionary syntax
Lists are mutable, non-primitive sequnces defined by square brackets `[]`. Their elements are comma-delimited, ordered, and heterogenous (i.e. any list element can be of any data type). One may retrieve and reasign elements from a list by indexing:

```Python
my_list = [True, 2, '3']
print(my_list[0])           # True

my_list[0] = {True: 1}
print(my_list)              # [{True: 1}, 2, '3']
```

Dictionaries are mutable, non-primitive mappings (or collection of key-value pairs) defined by curly brackets `{}`. Their elements are comma-delimited key-value pairs wherein each pair is separated by a colon. Dictionaries are unordered, so their values are accessed by their respective keys rather than indices. Dictionary values are heterogenous and their keys may be heterogenous, too, but their keys must be hashable. For our purposes, we just need to know that immutable objects are hashable. One may retrieve and reassign elements through key-based access:

```Python
my_dict = {
    True: 'I love you!',
    2: {'Krishna': 'Radha'},
    '3': ['rajas', 'tamas', 'sattva']
}
print(my_dict[True])                       # I love you!

my_dict[True] = 'I love you very much!'
print(my_dict)               

# {
# True: 'I love you very much!', 
# 2: {'Krishna': 'Radha'}, 
# '3': ['rajas', 'tamas', 'sattva']
# }
```

## list methods

### `len(list)`
Returns an integer whose value is the number of elements in `list`.

### `list.append(element_to_add)`
Mutates `list` by adding `element_to_add` to the end of `list`; returns `None`.

```Python
my_list = [1, 2, 3]
append_return_value = my_list.append(4)

print(append_return_value)    # None
print(my_list)                # [1, 2, 3, 4]
```

### `list.pop(index_to_remove)`
Mutates `list` by removing the element at index `index_to_remove`; returns the popped element. If no element is given, removes the last element.

```python
my_list = ['a', 'b', 'c', 'd']
pop_return_value = my_list.pop()

print(pop_return_value)    # d
print(my_list)             # ['a', 'b', 'c']

print(my_list.pop(0))      # a
print(my_list)             # ['b', 'c']
```

### `list.reverse()`
Mutates `list` by reversing the order of all elements; returns `None`.

```python
my_list = [1, 2, 3, 4, 5]
reverse_return_value = my_list.reverse()

print(reverse_return_value)    # None
print(my_list)                 # [5, 4, 3, 2, 1]
```

## dictionary methods

### `dict.keys()`
Returns a view object of the keys in `dict`; this object is tied to the keys in the dictionary it references and will reflect any mutations to those keys.

### `dict.values()`
Returns a view object of the values in `dict`; this object is tied to the values in the dictionary it references and will reflect any mutations to those values.

### `dict.items()`
Returns a view object of the `(key, value)` tuples in `dict`; this object is tied to the `(key, value)` tuples in the dictionary it references and will reflect any mutations to those elements.

### `dict.get('desired_key', 'alternative_output')`
Returns the value in `dict` associated with the `desired_key`, or if the `desired_key` is not present, returns the `alternative_output`.

```python
my_dict = {
    True: 'I love you!',
    2: {'Krishna': 'Radha'},
    '3': ['rajas', 'tamas', 'sattva'],
}

get = True
get_return_value = my_dict.get(get, f'No element {get}.')
print(get_return_value)    # I love you!

get = False
get_return_value = my_dict.get(get, f'No element {get}.')
print(get_return_value)    # No element False.
```

## slicing (strings, lists, tuples)
Slicing returns a portion of a given object as a new object. It uses the syntax `my_object[inclusive_start_index, exclusive_stop_index, step_size]`. One creates a reversed copy of a list by calling `my_object[::-1]`.

```python
my_tuple = (1, 2, 3, 4)
slicing_return_value = my_tuple[::-1]

print(slicing_return_value)    # (4, 3, 2, 1)
print(my_tuple)                # (1, 2, 3, 4)
```

## operators

### arithmetic: `+`, `-`, `*`, `/`, `//`, `%`, `**`
Arithmetic operators perform mathematical functions on Python's numeric values. Specifically... 
* Division (`/`) performs float division; the result is always a float regardless of the operand data types. 
* Integer division (`//`) returns the largest whole number less than or equal to the floating point result; the resulting data type depends on those of the operands. 
* Modulo (`%`) returns the remainder of a division operation; the resulting data type depends on those of the operands. 
* Exponentiation (`**`) performs an operation of the first operand raised to the power of the second operand; the resulting data type depends on those of the operands.


### string operators: `+`
Strings may be concatenated using the `+` operator. This always returns a new objects, because strings cannot be mutated.

```python
string1 = "I love you"
string2 = " so much!"
print(string1 + string2)    # I love you so much!
```

### list operators: `+`
List may be concatenated using the `+` operator. This may mutate a list if executed with augmented assignment, or create a new list if executed without augmented assignment.

```python
list1 = ['I', 'love', 'you']
print(list1)        # ['I', 'love', 'you']
print(id(list1))    # 4574835008

list2 = [4, 'ever']
print(list2)        # [ 4, 'ever']
print(id(list2))    # 4636840192

# list concatentation with augmented
# assignment mutates a list in-place
list1 += list2
print(list1)        # ['I', 'love', 'you', 4, 'ever']
print(id(list1))    # 4574835008

# list concatenation without augmented 
# assignment creates a new list
list1 = list1 + list2
print(list1)        # ['I', 'love', 'you', 4, 'ever', 4, 'ever']
print(id(list1))    # 4636805248
```

### comparison: `==`, `!=`, `<`, `>`, `<=`, `>=`
Comparison operations return a Boolean value that evaluates whether the comparison between their operands is `True` or `False`. The equality operator `==` evaluates the equality of element values, not the identities of objects in memory. It returns `True` if its operands have equal values and `False` if its operands have unequal values.

```python
# not equal to
print('4' != 4)     # True
print('a' < 'c')    # True
print('Z' < 'a')    # True

# integers in the range (-5, 256) inclusive
# are given a specific locations in memory
low1, high1 = -5, 256
low2, high2 = -5, 256

print(low1 == low2, high1 == high2)    # True True
print(low1 is low2, high1 is high2)    # True True

# integers outside of this range create a 
# new memory object when they are assigned
low3, high3 = -6, 257
low4, high4 = -6, 257

print(low3 == low4, high3 == high4)    # True True
print(low3 is low4, high3 is high4)    # False False
```

### logical: `and`, `or`, `not`
Logical operators evaluate the truthiness of their operands and return either the last evaluated element (`and`, `or`) or a Boolean value (`not`).

```python
print({} and [])            # {}
print({} or [])             # []
print(not "")               # True
print(not "I love you!")    # False
```

### identity: `is`, `is not`

The identity operator evaluates an object's location in memory, not its value. `is` returns `True` if two objects point to the same location in memory and `False` if two objects point to different memory location. The operator `is not` returns the opposite Boolean value of `is`. Use the function `id()` to evaluate an object's location in memory, represented as an integer. When objects share the same location in memory, this is known as aliasing.

Python employs "interning" in order to save memory space and improve performance. Python "interns", or reserves particular locations in memory, for each integer in the range (-5, 256) inclusive as well as some strings:

```python
# interned strings
a = 'Leah'
b = 'Leah'
c = b

print(a == b)            # True
print(a is b)            # True
print(id(a) == id(b))    # True

print(b == c)            # True
print(b is c)            # True
print(id(b) == id(c))    # True


# non-interned strings
d = 'Hello, Leah!'
e = 'Hello, Leah!'
f = e

print(d == e)            # True
print(d is e)            # False
print(id(d) == id(e))    # False

print(e == f)            # True
print(e is f)            # True
print(id(e) == id(f))    # True
```


### operator precedence<br>

Operators with higher precedence are evaluated before operatorss with lower precedence. Operands "bind more tightly" to operators of higher precedence, meaning operands belonging to two operators will evaluate within the context of the higher-precedence operator first.

Short-circuiting is a process by which `and` and `or` operations stop evaluating as soon as their evaluation condition is met; they do not continue to evaluate subsequent operands after the evaluation condition is met.

The operator precedence of comparison and logical operators is...

* left-to-right
* comparison (`==`, `!=`, `<`, `>`, `<=`, `>=`)
* `not`
* `and`
* `or`<br><br>

Let's see an example...

```python
# without short-circuiting
print(0 or 2 >= 1.5 and 'c' > 'a')

print(0 or ((2 >= 1.5) and ('c' > 'a')))
print(falsy or ((2 >= 1.5) and ('c' > 'a')))
print(falsy or (True and ('c' > 'a')))
print(falsy or (True and True))
print(falsy or True)
print(True)    # True

# with short-circuiting
print(1 or 2 >= 1.5 and 'c' > 'a')

print(1 or ((2 >= 1.5) and ('c' > 'a')))
print(truthy or ((2 >= 1.5) and ('c' > 'a')))
print(1)       # 1
```

Just for fun, here is operator precedence for all Python actions...

| Precedence | Operator | Description|
| :--- | :--- | :--- |
| 1 | `(`expressions...`)`, `[`expressions...`]`, `{`key`:`value...`}`, `{`expressions...`}` | Binding or parenthesized expression, list display, dictionary display, set display |
| 2 | x`[index]`, x`[index:index]`, x`(arguments...)`, x`.attribute` | Subscription, slicing, call, attribute reference |
| 3 | `await` x | Await expression |
| 4 | `**` | Exponentiation |
| 5 | `+`x, `-`x, `~`x | Positive, negative, bitwise NOT |
| 6 | `*`, `@`, `/`, `//`, `%` | Multiplication, matrix multiplication, division, floor division, remainder (modulo) |
| 7 | `+`, `-` | Addition and subtraction |
| 8 | `<<`, `>>` | Shifts |
| 9 | `&` | Bitwise AND |
| 10 | `^` | Bitwise XOR |
| 11 | `\|` | Bitwise OR |
| 12 | `in`, `not in`, `is`, `is not`, `<`, `<=`, `>`, `>=`, `!=`, `==` | Comparisons, including membership tests and identity tests |
| 13 | `not` x | Boolean NOT |
| 14 | `and` | Boolean AND |
| 15 | `or` | Boolean OR |
| 16 | `if` - `else` | Conditional expression |
| 17 | `lambda` | Lambda expression |
| 18 | `:=` | Assignment expression |

## mutability and immutability
Mutability refers to the abilty to mutate an object in memory once it has been initialized. Mutable objects can be changed "in-place", or at their location in memory, after they have been initialized. Mutable objects include lists, dictionaries, sets, and functions. Immutable objects cannot be changed in-place once they have been initialized. Immutable objects include integers, floats, strings, Booleans, ranges, tuples, frozensets, and `None`.


```python
# mutability
my_list = [1, 2, 3]
print(my_list)        # [1, 2, 3]
print(id(my_list))    # 4415656448

my_list += [4]
print(my_list)        # [1, 2, 3, 4]
print(id(my_list))    # 4415656448

# immutability
my_int = 4
print(my_int)         # 4
print(id(my_int))     # 4315406592

my_int += 4
print(my_int)         # 8
print(id(my_int))     # 4315406720
```

## variables
Variables are names that we give to objects in memory.

### naming conventions
Variables are named with `snake_case` using all lowercase letters and underscores between words. One can include digits within a variable name, but they may not start with a digit.

### initialization, assignment, and reassignment 
Variables are intialized and assigned by setting a variable name equal to a value. Reassign a variable by setting a variable name that has already been used equal to another value. Variable reassignment (without augmented assignment) almost always creates a new object in memory, even if the object being reassigned is mutable.

```python
my_var = ['Hello']
print(id(my_var))    # 4395536512

my_var = ['Hello']
print(id(my_var))    # 4395536192
```

The exception to this occurs with interned values. When a value is interned, any new variable assigned to that value becomes an alias for its location in memory.

```python
# The string object 'Hello' is interned
my_var = "Hello"
print(id(my_var))        # 4421994752

my_new_var = "Hello"
print(id(my_new_var))    # 4421994752

my_var = "Hi"
print(id(my_var))        # 4421993840


# The string object 'Hello, world!' is not interned
my_var = "Hello, world!"
print(id(my_var))        # 4422021872

my_var = "Hello, world!"
print(id(my_var))        # 44422021936
```

### scope
Variable scope describes where in code a variable can be accessed by name. A particular variable's scope depends on where it was initialized. Variables initialized within an outer scope are accessible within all its nested inner scopes; therefore, variables initialized within the global scope are accessible everywhere in a program. However, variables initialized in an inner scope are not accessible to their outer scopes unless initialized using the `global` or `nonlocal` keywords.

### `global` keyword 
The `global` keyword alerts Python to local for a variable name in the global scope, or if a name is yet unused, to add the name to the global scope. We use the `global` keyword within functions to avoid variable shadowing or to initialize variables within functions that we want to access in the global scope

```python
# avoid variable shadowing
greeting = "Hello"

def say_hi(name):
    global greeting
    greeting = "Hi"
    print(f'{greeting}, {name}!')

say_hi("Leah")     # "Hi, Leah!"
print(greeting)    # "Hi"


# initialize a variable within a function
# that we want to access in the global scope
def initialize_greeting():
    global greeting
    greeting = "Ahoy!"

initialize_greeting()
print(greeting)    # "Ahoy!"
```

### variables as pointers 
Variables are described as "pointers" because they reference or "point to" a location in memory or "address space" that contains the object assigned to the value. One can also describe variables as "references", which is used interchangably with "poiners". Let's see an example...

```python
# this is not a reassignment of the 'my_list' variable;
# it's a mutation of the list object referenced by 'my_list'
my_list = ['I', 'love', 'you']
print(id(my_list))       # 4415785728
print(id(my_list[1]))    # 4411175392

my_list[1] = 'adore'
print(id(my_list))       # 4415785728
print(id(my_list[1]))    # 4411170400

print(my_list)

# (it's also a reassignment of the list object 
# element at index 1, but it's not a mutation of
# that element because strings are immutable)
```

### variable shadowing
Variable shadowing occurs when a variable within an outer scope shares a name with a variable within it's inner scope. When this variable is invoked in the inner scope, it points to the object it was assigned in the inner scope, rather than in the outer scope, and "shadows" the object it was assigned in the outer scope. For example...

```python
greeting = "Hello"

def say_hi(name):
    greeting = "Hi"
    print(f'{greeting}, {name}!')

say_hi("Leah")     # "Hi, Leah!"
print(greeting)    # "Hello"
```

The effect of variable shadowing in this example is that, even though the global variable `greeting` continually points to the string object `"Hello"`, it is shadowed by the local variable `greeting` within the function `say_hi`. Therefore, when we invoke `say_hi`, the output is `"Hi, Leah!"`. <br><br>

## conditionals and loops
Conditionals take part in the control flow of a program. They use a combination of `if`, `elif`, and `else` statements along with comparison, logical, and membership operators (`==`, `!=`, `<`, `<=`, `>`, `>=`, `in`, `not in`, `is`, `is not`, `and`, `or`, `not`) in order to direct Python to certain operations under certain conditions. Loops are an efficient way to iterate over a sequence of objects, or continuously while a condition is met, and perform an operation at each iteration. There are two types of loops: `for` and `while`.

### `for` 
A `for` loop iterates over a sequence, such as a range, and performs a task during each iteration. The `for` loop ends when it has iterated over all the items in the sequence and performed the respective tasks.

### `while`
A `while` loop evaluates a conditional statement and performs its tasks as long as the statement evaluates to `True`. The `while` loop ends when the condition is no longer met.<br><br>

## `print()` and `input()`
The built-in functions `print()` and `input()` either output data to the console or input data from the console. They involve implicit coersion, as `print()` coerces all data types to strings before outputing them to the console, and `input()` coerces all data types to strings before assigning them to a variable within a function.
```python
def say_hi():
    # input() pauses the function execution 
    # to receive an input from the console
    name = input("What's your name? ")       # What's your name?  Leah

    # input() coerces all inputs to strings
    age = input("What's your age? ")         # What's your age?  30
    
    print(f"Hi, {name}! Welcome to {age}!")

say_hi()    # Hi, Leah! Welcome to 30!
```


## exceptions (when they will occur and how to handle them)
Exceptions occur when there is code that Python cannot interpret. The seven types of excepions discussed in Launch School are `ZeroDivisionError`, `KeyError`, `IndexError`, `NameError`, `TypeError`, `ValueError`, and `SyntaxError`. Exception handling can be broken down into four steps:

1. **Try:** This block contains the code that might raise an exception.
2. **Except:** If an exception is raised in `try` block, Python will look for a matching `except` block that can handle that specific type of exception. If a match is found, the code within the corresponding `except` block will execute. There can be multiple `except` blocks following a `try` block.
3. **Else:** This block is executed only if no exceptions raised in `try` block and, thus, if the `except` block is not executed.
4. **Finally:** This block is always executed, whether errors raised or not. Used for cleanup operations or mandatory tasks.

```python
def invalid_number(number_string):
    try: 
        print("Executing try block...")
        int(number_string)
    except TypeError:
        print("Executing TypeError exception block...")
        return True
    except ValueError:
        print("Executing ValueError exception block...")
        return True
    else:
        print("Executing else block...")
    finally:
        print("Executing finally block...")

    return False

print(invalid_number("10"))
# Executing try block...
# Executing else block...
# Executing finally block...
# False

print(invalid_number("10.0"))
# Executing try block...
# Executing ValueError exception block...
# Executing finally block...
# True

print(invalid_number([10]))
# Executing try block...
# Executing TypeError exception block...
# Executing finally block...
# True

```

## functions:
Functions create reusable pieces of code that can be invoked with at each instance of execution.

### definitions and calls 
Functions are defined using the `def` keyword followed the function name in `snake_case`, parentheses, and a colon. Their parameters are declared within the parenteses following the function name. Functions are called using the function name and any input arguments, if the function excepts them.

```python
# this is the function definition
def say_hi(name):
    print(f'Hi, {name}!!!')

# this is the function call
say_hi('Leah')    # Hi, Leah!!!
```

### return values
Functions pass return values to their caller eitherwhen they reach the end of their body, or when they encounter the `return` keyword. This return statement immediately exits the function and outputs a return value. It may be an explicit return value, specified directly after the `return` keyword, or an implicit return value (`None`) if none is specified. It's important to remember that all functions return something unless they raise an exception; if no return value is specified, the function returns `None`.

### parameters vs. arguments 
Parameters are declared within the function definition; they are placeholders for potential arguments passed into a function when it is invoked. Arguments are the actual values that get passed in during the function invocation.

```python
# the function definition of 'say_hi' declares 
# one parameter as a local variable: 'name'
def say_hi(name):
    print(f'Hi, {name}!!!')

# the function invocation of 'say_hi' passes
# one argument: the string 'Leah'
say_hi('Leah')    # Hi, Leah!!!
```

### nested functions
When a function is defined within another function, it is known as a nested function. Variable scoping rules day that variables initialized within an outer function can be accessed in their nested functions, but variables initialized within a nested function cannot be accessed by their enclosing functions. Nested functions can shadow variables within their enclosing functions as well.

### output vs. return values, side effects 
Function outputs are anything that is displayed to the console during the function's execution. For example, if anything is printed within a function body, the printed message is considered an output. Return values, however, are specifically the values within the function's return statement; they are returned to the caller, not displayed in the console. Side effects are any outputs or actions that are not returned in the return statement. Function are said to have side effects if they...

* reassign any non-local variables.
* modify the value of any data structure passed as an argument or accessed directly from the outer scope (e.g., mutating a list).
* read from / write to a file, network connection, browser, or the system hardware, including printing and reading input from the console.
* raise exceptions without handling them.
* call other functions that have side effects.


## expressions and statements
Expressions are parts of code that are evaluated to produce a new object. Remember that expressions produce a value that can then be assigned to a variable, passed to a function / method, or returned by a function / method. Examples of expressions include...

* literals: `0`, `1.234`, `Leah`, `True`, `None`
* variable references: `foo` or `name` when these variables have already been defined
* arithmetic operations: `a - b`, `a * b + 12`
* comparison operations: `'x' != 'y'`, `5 <= 10`
* string operations: `'hello' + ', world!'`, `iloveyou * 1000`
* function calls: `print('i love you')`, `len('i love you')`
* any combinatio of the above that evaluates to a single object

Statements are instructions that tell Python to perform an action and, importantly, do not output any value. Examples of statements include...

* assignment: `x = 1`
    * interestingly, both `x` and `1` are expressions, but `x = 1` is a statement
* control flow: `if`, `elif`, `else`, `while`, `for`, etc.
* function definitions: `def`
* return statements: `return`
* import statements: `import`