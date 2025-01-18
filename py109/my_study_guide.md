# PY 109 Study Guide: Python Basics

### naming convention: legal vs. idiomatic, illegal vs. non-idiomatic<br>`CONFIDENT`

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

### type coercions: explicit (e.g., using `int()`, `str()`) and implicit<br>`ALMOST THERE`

Type coercion involves changing an object value from one data type to another. This can happen explicitly with constructor function...
* `int()`, `float()`, `str()`, `list()`, `dict()`, `tuple()`, `set()`, `frozenset()` convert objects to integers, floats, strings, lists, dictionaries, tuples, sets, and frozensets, respectively.<br><br>

Or it can happen implicitly in a variety of ways:
* Mathematical statements involving plain division may convert to a `float`: `5 / 2 = 2.5`
* Mathematical statements involving type mixing may convert to a `float`: `4 + 2.0 = 6.0`
* Invoking the `print()` function implicitly converts all input to a string object before printing.<br><br>

### numbers<br>`ALMOST THERE`
There are several types of numbers in Python; the ones we primarily consider in Launch School are integers (`int`) and floats (`float`). Integers are whole numbers and do not include a decimal point. Floats are real numbers and always include a decimal point, even if there is not decimal value. Both integers and floats are immutable, primitive data types.

* `int`: `1`, `-1`
* `float`: `1.0`, `-1.0`, `12.34`<br><br>

With respect to large numbers, one may represent commas with underscores:
* `1000 == 1_000` returns `True`
* `123.456_789 == 123.456789` returns `True`<br><br>

Furthermore, one may represent large floats with scientific notation, but large integers are never represented with scientific notation:
* `print(float(3e16))` returns `3e16`
* `print(int(3e16))` returns `30000000000000000`<br><br>

### strings<br>`CONFIDENT`
Strings are immutable, primitive text sequences. They can be represented with single quotes (`'hi'`), double quotes (`"hello"`), or triple single quotes (`'''`) or triple double quotes (`"""`)for multi-line strings. If a quote contains both single and double quotes in its body, you may use triple quotes or escape characters:
* `'''What d'you mean by "closed"?'''`
* `"What d'you mean by \"closed\"?"`<br><br>

In many cases, strings share the same behavior as sequences. They can be...
* indexed: `'hello'[0] == 'h'` returns `True`; `'hello'[-4] == 'e'` returns `True`
* sliced: `'hello'[0:2] == 'he'` returns `True`; `'hello'[::2] == 'hlo'` returns `True`<br><br>

### f-strings<br>`CONFIDENT`
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

### string methods
As immutable objects, strings cannot be mutated under any circumstances. However, string methods can be performed on strings, returning a new string object with the intended modifications.<br><br>

#### `str.capitalize()`
Returns a copy of `str` with the first letter capitalized and the remaining letters in lowercase.<br><br>

#### `str.swapcase()`
Returns a copy of `str` with cases completely swapped: lowercase characters becomes uppercase and uppercase characters become lowercase.<br><br>


#### `str.upper()`
Returns a copy of `str` with all characters in uppercase.<br><br>

#### `str.lower()`
Returns a copy of `str` with all characters in lowercase.<br><br>

#### `str.isalpha()`
Returns `True` if all characters in `str` are alphabetic, or `False` if any character is non-alphabetic. *Note:* Python is aware of all Unicode characters, even those that are not in English. To include only ascii characters, use `str.isalpha() and str.isascii()`.<br><br>

#### `str.isdigit()`
Returns `True` if all characters in `str` are digits, or `False` if any character is not a digit.<br><br>

#### `str.isalnum()`
Returns `True` if all characters in `str` are alphabetic or digits, or `False` if any character is neither alphabetic nor a digit.<br><br>

#### `str.islower()`
Returns `True` if all characters in `str` are lowercase, or `False` if any character is not lowercase.<br><br>

#### `str.isupper()`
Returns `True` if all characters in `str` are uppercase, or `False` if any character is not uppercase.<br><br>

#### `str.isspace()`
Returns `True` if all characters in `str` are whitespace characters, including space (`' '`), newline (`'\n'`), tab (`'\t'`), carriage return (`'\r'`), vertical tab (`'v'`), and form feed (`'f'`), as well as foreign whitespace characters, or `False` where this is not the case.<br><br>

#### `str.strip('characters')`
Returns a copy of `str` with leading and trailing whitespace characters removed. This method can take an argument such as `str.strip('+')` to remove all leading and trailing instances of those characters from the copied string. *Note:* This method removes characters, not substrings.
```Python
my_string = 'abbcccxyzaaabbc'
my_string.strip('abc')           # 'xyz'
```

#### `str.rstrip('characters')`
Returns a copy of `str` with trailing whitespace (default) or chosen characters removed.<br><br>

#### `str.lstrip('characters')`
Returns a copy of `str` with leading whitespace (default) or chosen characters removed.<br><br>

#### `str.replace('old', 'new')`
Returns a copy of `str` with the first argument replaced by the second argument.
```Python
my_string = 'cat'
my_string.replace('c', 'h')    # 'hat'
```

#### `str.split('character')`
Returns a list of the words in `str`, using spaces (default) as an indicator of a new word, or a given character.
```Python
my_string = 'I love you'
print(my_string.split())            # ['I', 'love', 'you']

my_next_string = 'I + love + you'
print(my_next_string.split('+'))    # ['I ', ' love ', ' you']
```

#### `str.find('character_or_string')`
Returns the first index at which the given character or string is found within `str`.<br><br>

#### `str.rfind('character_or_string')`
Returns the first index at which the given character or string is found within `str`, searching from right to left. *Note:* This method returns the left-to-right index of `str`, even though it searches for the given input from right to left.<br><br>

#### boolean vs. truthiness
Booleans are immutable, primitive objects representing binary states. There are two boolean values: `True` and `False`. They often appear as the return value of methods or logical / comparison operations. In mathematical expressions, `True` evaluates to `1` and `False` evaluates to `0`.

Truthiness is a way of describing how a value behaves in a Boolean context. When an object contains a non-zero or non-empty value, we say that that value "is truthy" or "evaluates to true". When the object contains a zero, empty, or `None` value, we say that that value "is falsy" or "evaluates to false". Examples of falsy values include:
* `False`, `None`
* `0`, `0.0`, and other numerical representations of zero
* empty (text) sequences: `""`, `[]`, `()`, `{}`, `range(0)`, `set()`, `frozenset()`
* any custom data types defined as falsy<br><br>


#### `None`
`None` is an immutable data type used to describe an object with an absent value. The default return value for custom functions, as well as many methods that mutate mutable objects is `None`. Launch School is inconclusive about whether `None` is a primitive or non-primitive data type.<br><br>

#### ranges
Ranges are immutable, non-primitive sequences that increment integer values from one endpoint to another. Ranges are "lazy sequences" meaning that they do not create element values until they are called, usually by iterating them in a `for` loop or coercing them into another data type,. Their syntax is `range(inclusive_starting_integer, exclusive_ending_integer, step_size)`. Make a decending range by inputing a negative step size and a startpoint greater than the endpoint. If the step size is negative and the startpoint is less than the endpoint, or if the startpoint is equal to the endpoint no matter the step size, Python will return an empty range.
```Python
print(range(2, 25, 4))            # range(2, 25, 4)
print(list(range(2, 25, 4)))      # [2, 6, 10, 14, 18, 22]

print(range(1, 10, -1))           # range(1, 10, -1)
print(list(range(1, 10, -1)))     # []

print(range(10, 10, -1))          # range(10, 10, -1)
print(list(range(10, 10, -1)))    # []
```

#### list and dictionary syntax

