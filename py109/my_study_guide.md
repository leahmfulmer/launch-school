# PY 109 Study Guide: Python Basics

### naming convention: legal vs. idiomatic, illegal vs. non-idiomatic
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

### type coercions: explicit (e.g., using `int()`, `str()`) and implicit
Type coercion involves changing an object value from one data type to another. This can happen explicitly through constructor functions:
* `int()`, `float()`, `str()`, `list()`, `dict()`, `tuple()`, `set()`, `frozenset()` converts an object to a string
*

### Explicit 

