# Define a prompt function
def prompt(input):
    print(f'==> {input}')

# Define an invalide_number function
def invalid_number(num_str):
    try:
        int(num_str)
    except ValueError:
        try:
            float(num_str)
        except ValueError:
            return True

    return False

# Welcome
prompt('Welcome to Calculator!')

# Let calculator run until user stops it
while True:
    
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
    prompt("Your options are '+' (addition), '-' (subtraction),'*' (multiplation),")
    prompt("and '/' (division). You may type your selection without quotation marks.")
    operation = input()

    while operation not in ['+', '-', '*', '/']:
        prompt("Hmm... that doesn't look like a valid operation. Please try again.")
        operation = input()

    # Perform the operation on the two numbers.
    if type(num1) == 'int':
        num1 = int(num1)
    else:
        num1 = float(num1)

    if type(num2) == 'int':
        num2 = int(num2)
    else:
        num2 = float(num2)

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
    prompt(' ')

    # Ask if user would like to perform another calculation.
    prompt("Would you like to perform another calculation?")
    prompt("Your options are 'yes' or 'no'. You may type your response without quotation marks.")
    response = input()

    while response not in ['yes', 'no']:
        prompt("Hmm... that doesn't look like a valid operation. Please try again.")
        response = input()

    if response != 'yes':
        break
