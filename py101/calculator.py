# Define a prompt function
def prompt(input):
    print(f'==> {input}')

# Define an invalide_number function
def invalid_number(num_str):
    try:
        int(num_str)
    except ValueError:
        return True

    return False

# Welcome
prompt('Welcome to Calculator!')

# Ask the user for the first number.
prompt("What's the first number?")
num1 = input()

while invalid_number(num1):
    prompt("Hmm... that doesn't look like a valid number. Please try again.")
    num1 = input()

# Ask the user for the second number.
prompt("What's the second number?")
num2 = input()

while invalid_number(num2):
    prompt("Hmm... that doesn't look like a valid number. Please try again.")
    num2 = input()

# Report numbers
prompt(f'Your number are {num1} and {num2}.')


# Ask the user for an operation to perform.
prompt("What operation would you like to perform?")
prompt("""Your options are '+' (addition), '-' (subtraction),'*' (multiplation),
and '/' (division). You may type your selection without quotation marks.""")
operation = input()

while operation not in ['+', '-', '*', '/']:
    prompt("Hmm... that doesn't look like a valid operation. Please try again.")
    operation = input()

# Perform the operation on the two numbers.
num1 = int(num1)
num2 = int(num2)

match operation:
    case '+':
        result = num1 + num2
    case '-':
        result = num1 - num2
    case '*':
        result = num1 * num2
    case '/':
        result = num1 / num2

# Print the result to the terminal.
prompt(f'The result is: {result}')
